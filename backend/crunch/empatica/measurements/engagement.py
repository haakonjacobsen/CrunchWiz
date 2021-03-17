import numpy as np

"""
TODO remove this
from article about engagement
https://www.researchgate.net/publication/272747425_Using_Electrodermal_Activity_to_Recognize_Ease_of_Engagement_in_Children_during_Social_Interactions

From the tonic and phasic components of each child’s EDA
signal, we extracted the following IF features: mean,
standard deviation, area under the curve, relative positions
of maximum and minimum values, slope (estimated by
linear interpolation), average number of peaks, and average
of the peaks amplitudes.

slope is linear interpolation of
    1) min point
    2) (max point - min point) / 2
"""

""" Constants """
DT = 20  # delta time, 20 second moving time window
FQ = 4  # frequency of data points, 4 per seconds
NR_DATA_POINTS = DT * FQ + 1  # The number of data points after mean filter is applied
MEAN_KERNEL_WIDTH = 5 * FQ  # The width (data points) of the mean kernel
NR_DATA_POINTS_WITH_KERNEL = NR_DATA_POINTS + 2 * MEAN_KERNEL_WIDTH  # The total number of data points before mean kernel
ONSET_THRESHOLD = 0.01  # the threshold in microsiemens required to classify an onset of a peak
OFFSET_THRESHOLD = 0  # the threshold in microsiemens required to classify an offset of a peak


def compute_engagement(eda) -> float:
    """
    Calculates the engagement based on EDA features

    Takes in the last 121 data points, which corresponds ot 30 seconds of data. Extracts the tonic component of the
    EDA data by using a mean moving window of length 10 seconds, and then removing first and last 5 seconds
    worth of data. Extracts the phasic component from the difference of the eda signal and the tonic component.
    From the phasic component we calculate peaks and slope, from the tonic component we calculate area under the curve.

    :param eda: list of eda data points
    :type eda: list
    :return: engagement - sum of normalized features related to engagement
    """
    assert len(eda) == NR_DATA_POINTS_WITH_KERNEL

    # find tonic and phasic components
    mean_arr = _mean_filter(eda)
    relevant_eda = eda[MEAN_KERNEL_WIDTH: -MEAN_KERNEL_WIDTH]
    tonic = mean_arr - abs(min(relevant_eda - mean_arr))
    phasic = relevant_eda - tonic

    # features
    peak_start, peak_end = _find_peaks(relevant_eda - mean_arr)
    amplitude = _find_amplitude(peak_start, peak_end, phasic)
    nr_peaks = sum(peak_start)
    auc = _area_under_curve(tonic)

    # TODO remove this when we don't want to visualize
    # _plot(tonic, phasic, peak_start, peak_end, amplitude, relevant_eda)

    # TODO fix proper calculation and normalization and stuff
    engagement = nr_peaks + auc

    return engagement


def _mean_filter(eda) -> np.array:
    """ Compute the mean eda signal, using a mean kernel of 10 seconds width """
    mean_arr = np.array([])
    for i in range(MEAN_KERNEL_WIDTH, NR_DATA_POINTS_WITH_KERNEL - MEAN_KERNEL_WIDTH):
        mean = np.mean(eda[i - MEAN_KERNEL_WIDTH: i + MEAN_KERNEL_WIDTH + 1])
        mean_arr = np.append(mean_arr, mean)
    return mean_arr


def _find_peaks(modified_phasic) -> (np.ndarray, np.ndarray):
    """ Find the position of peak start and peak ends on the phasic signal """
    peak_start = np.zeros(NR_DATA_POINTS)
    peak_end = np.zeros(NR_DATA_POINTS)
    rising = False

    # identify if start is peak
    if ONSET_THRESHOLD < modified_phasic[0] < modified_phasic[1]:
        peak_start[0] = 1
        rising = True

    for i in range(NR_DATA_POINTS - 1):
        # peak starts from the point it gets above the onset threshold
        if modified_phasic[i] < ONSET_THRESHOLD < modified_phasic[i + 1] and not rising:
            peak_start[i + 1] = 1
            rising = True
        # peak ends from the point it dips below the offset threshold
        elif modified_phasic[i] > OFFSET_THRESHOLD > modified_phasic[i + 1] and rising:
            peak_end[i + 1] = 1
            rising = False

    return peak_start, peak_end


def _find_amplitude(peak_start, peak_end, phasic) -> float:
    """ Find the total amplitude of the highest points of each peak """
    amplitude = 0
    for i in range(NR_DATA_POINTS):
        # if we found a peak start
        if peak_start[i] == 1:
            j = i
            # find the peak end (or end of data points)
            while j < NR_DATA_POINTS and peak_end[j] != 1:
                j += 1
            # find the highest point of phasic in the range from the start of peak to end of peak
            amplitude += max(phasic[i:j + 1])

    return amplitude


def _area_under_curve(tonic) -> float:
    """ Computes the area under the curve of the tonic signal, using trigonometry """
    auc = 0
    for i in range(NR_DATA_POINTS - 1):
        # first data point
        y1 = tonic[i]
        # second datapoint
        y2 = tonic[i + 1]
        # change in y
        dy = y2 - y1
        # change in x
        dx = 1 / FQ

        area_square = y1 * dx
        area_triangle = dy * dx / 2
        auc += area_square + area_triangle

    return auc / DT


"""
import matplotlib.pyplot as plt
# Mostly for debugging purposes, to visualize eda, tonic, phasic, peaks and amplitude
def _plot(tonic, phasic, peak_start, peak_end, amplitude, eda):
    # TIME AXIS
    y = [i * 0.25 for i in range(NR_DATA_POINTS)]

    plt.figure(1, figsize=(20, 5))
    plt.plot(y, eda, label="eda")
    plt.plot(y, phasic, label="phasic")
    plt.plot(y, peak_start, label="peak start")
    plt.plot(y, peak_end, label="peak end")
    plt.plot(y, tonic, label="tonic")
    plt.plot(y, [amplitude for _ in range(NR_DATA_POINTS)], label=f"total amplitude={round(amplitude, 3)}")
    plt.legend()
    plt.show()
"""
