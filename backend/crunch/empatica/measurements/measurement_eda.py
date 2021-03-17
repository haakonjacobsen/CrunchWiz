import numpy as np
import matplotlib.pyplot as plt

"""
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

# delta time, 20 second moving time window
DT = 20
# frequency of data points, 4 per seconds
FQ = 4
# The number of data points in our tonic and phasic measurements, i.e after mean filter
NR_DATA_POINTS = DT * FQ + 1
# The width (data points) of the mean kernel, so we only use the first and last 5 seconds for interpolation
MEAN_KERNEL_WIDTH = 5 * FQ
# The total number of data points before we have used mean kernel
NR_DATA_POINTS_WITH_KERNEL = NR_DATA_POINTS + 2 * MEAN_KERNEL_WIDTH
# the threshold in microsiemens required to classify an onset of a peak
ONSET_THRESHOLD = 0.01
# the threshold in microsiemens required to classify an offset of a peak
OFFSET_THRESHOLD = 0


# Takes in a 121 data points (30 seconds)
# Measures the tonic EDA from the middle 20 seconds
# Uses the first 5 and last 5 seconds to interpolate the tonic signal more accurately
def calculate_arousal(eda):
    assert len(eda) == NR_DATA_POINTS_WITH_KERNEL

    # compute the mean with kernel of 5 second width, so we are left with 20 seconds in the middle
    mean_arr = _mean_filter(eda)

    # Get the middle 20 seconds of the EDA
    relevant_eda = eda[MEAN_KERNEL_WIDTH: -MEAN_KERNEL_WIDTH]

    # Tonic is the mean shifted so it is below eda
    tonic = mean_arr - abs(min(relevant_eda - mean_arr))

    # phasic is difference of eda and tonic
    phasic = relevant_eda - tonic

    # finds the peak from the data points
    peak_start, peak_end = _find_peaks(relevant_eda - mean_arr)

    # finds the total amplitude, also called EDA positive change
    amplitude = _find_amplitude(peak_start, peak_end, phasic)

    # The number of peaks in the 20 second window, counted from the number of peak starts we find
    nr_peaks = sum(peak_start)

    # area under curve of the tonic EDA, normalized for per second
    auc = _area_under_curve(tonic)

    # TODO remove this when we don't want to visualize
    # _plot(tonic, phasic, peak_start, peak_end, amplitude, relevant_eda)

    return amplitude, nr_peaks, auc


# Compute mean filter from the eda, reduce from 30 seconds of data points to 20 seconds, because of kernel width
def _mean_filter(eda):
    mean_arr = np.array([])
    for i in range(MEAN_KERNEL_WIDTH, NR_DATA_POINTS_WITH_KERNEL - MEAN_KERNEL_WIDTH):
        mean = np.mean(eda[i - MEAN_KERNEL_WIDTH: i + MEAN_KERNEL_WIDTH + 1])
        mean_arr = np.append(mean_arr, mean)
    return mean_arr


# Finds the position of the start and end of peaks
# modified phasic is basically the same as phasic, except it is centered around 0 (ish)
def _find_peaks(modified_phasic):
    peak_start = np.zeros(NR_DATA_POINTS)
    peak_end = np.zeros(NR_DATA_POINTS)

    # separate logic for the start, since we want to classify start of the peak even if it starts above threshold
    if ONSET_THRESHOLD < modified_phasic[0] < modified_phasic[1]:
        peak_start[0] = 1

    # Find the onset and offset points
    for i in range(NR_DATA_POINTS - 1):
        # peak starts from the point it gets above the onset threshold
        if modified_phasic[i] < ONSET_THRESHOLD < modified_phasic[i + 1]:
            peak_start[i + 1] = 1
        # last point was above offset threshold and current point is below
        elif modified_phasic[i] > OFFSET_THRESHOLD > modified_phasic[i + 1]:
            peak_end[i + 1] = 1

    return peak_start, peak_end


def _find_amplitude(peak_start, peak_end, phasic):
    # total amplitude of the peaks
    amplitude = 0

    # find amplitudes
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


def _area_under_curve(tonic):
    auc = 0
    # goes through adjacent pairs of data points, compute auc using linear trigonometry
    for i in range(NR_DATA_POINTS - 1):
        # first data point
        y1 = tonic[i]
        # second datapoint
        y2 = tonic[i + 1]
        # chance in y
        dy = y2 - y1
        # change in x
        x = 1 / FQ

        area_square = y1 * x
        area_triangle = dy * x / 2
        auc += area_square + area_triangle

    # TODO what value to return, either auc for 20 seconds, or normalized for 1 second,
    #  or normalized for 1 frequency (0.25 seconds)
    return auc / DT


"""
# TODO remove this when production ready
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
