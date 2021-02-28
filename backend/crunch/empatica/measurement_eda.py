import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import deque


# TODO slope of phasic eda, unsure about this, need to ask customer
# TODO proper comments
# Note somewhere that the results are at least 5 seconds delayed, because of interpolation

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
class EDA:
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
    def calculate_measurements(self, eda):
        assert len(eda) == self.NR_DATA_POINTS_WITH_KERNEL

        # compute the mean with kernel of 5 second width, so we are left with 20 seconds in the middle
        mean_arr = self._mean_filter(eda)

        # Get the middle 20 seconds of the EDA
        relevant_eda = eda[self.MEAN_KERNEL_WIDTH: -self.MEAN_KERNEL_WIDTH]

        # Tonic is the mean shifted so it is below eda
        tonic = mean_arr - abs(min(relevant_eda - mean_arr))

        # phasic is difference of eda and tonic
        phasic = relevant_eda - tonic

        # finds the peak from the data points
        peak_start, peak_end = self._find_peaks(relevant_eda - mean_arr)

        # finds the total amplitude, also called EDA positive change
        amplitude = self._find_amplitude(peak_start, peak_end, phasic)

        # The number of peaks in the 20 second window, counted from the number of peak starts we find
        nr_peaks = sum(peak_start)

        # area under curve of the tonic EDA, normalized for per second
        auc = self._area_under_curve(tonic)

        # TODO remove this when we don't want to visualize
        self._plot(tonic, phasic, peak_start, peak_end, amplitude, relevant_eda)

        return amplitude, nr_peaks, auc

    # Compute mean filter from the eda, reduce from 30 seconds of data points to 20 seconds, because of kernel width
    def _mean_filter(self, eda):
        mean_arr = np.array([])
        for i in range(self.MEAN_KERNEL_WIDTH, self.NR_DATA_POINTS_WITH_KERNEL - self.MEAN_KERNEL_WIDTH):
            mean = np.mean(eda[i - self.MEAN_KERNEL_WIDTH: i + self.MEAN_KERNEL_WIDTH + 1])
            mean_arr = np.append(mean_arr, mean)
        return mean_arr

    # Finds the position of the start and end of peaks
    # modified phasic is basically the same as phasic, except it is centered around 0 (ish)
    def _find_peaks(self, modified_phasic):
        peak_start = np.zeros(self.NR_DATA_POINTS)
        peak_end = np.zeros(self.NR_DATA_POINTS)

        # separate logic for the start, since we want to classify start of the peak even if it starts above threshold
        if self.ONSET_THRESHOLD < modified_phasic[0] < modified_phasic[1]:
            peak_start[0] = 1

        # Find the onset and offset points
        for i in range(self.NR_DATA_POINTS - 1): # CHECK I AND I + 1
            # peak starts from the point it gets above the onset threshold
            if modified_phasic[i] < self.ONSET_THRESHOLD < modified_phasic[i + 1]:
                peak_start[i + 1] = 1
            # last point was above offset threshold and current point is below
            elif modified_phasic[i] > self.OFFSET_THRESHOLD > modified_phasic[i + 1]:
                peak_end[i + 1] = 1

        return peak_start, peak_end

    def _find_amplitude(self, peak_start, peak_end, phasic):
        # total amplitude of the peaks
        amplitude = 0

        # find amplitudes
        for i in range(self.NR_DATA_POINTS):
            # if we found a peak start
            if peak_start[i] == 1:
                j = i
                # find the peak end (or end of data points)
                while j < self.NR_DATA_POINTS and peak_end[j] != 1:
                    j += 1
                # find the highest point of phasic in the range from the start of peak to end of peak
                amplitude += max(phasic[i:j + 1])

        return amplitude

    def _area_under_curve(self, tonic):
        auc = 0
        # goes through adjacent pairs of data points, compute auc using linear trigonometry
        for i in range(self.NR_DATA_POINTS - 1):
            # first data point
            y1 = tonic[i]
            # second datapoint
            y2 = tonic[i + 1]
            # chance in y
            dy = y2 - y1
            # change in x
            x = 1/self.FQ

            area_square = y1 * x
            area_triangle = dy * x / 2
            auc += area_square + area_triangle

        # TODO what value to return, either auc for 20 seconds, or normalized for 1 second, or normalized for 1 frequency (0.25 seconds)
        return auc / self.DT

    # TODO remove this when production ready
    # Mostly for debugging purposes, to visualize eda, tonic, phasic, peaks and amplitude
    def _plot(self, tonic, phasic, peak_start, peak_end, amplitude, eda):
        # TIME AXIS
        y = [i * 0.25 for i in range(self.NR_DATA_POINTS)]

        plt.figure(1, figsize=(20, 5))
        plt.plot(y, eda, label="eda")
        plt.plot(y, phasic, label="phasic")
        plt.plot(y, peak_start, label="peak start")
        plt.plot(y, peak_end, label="peak end")
        plt.plot(y, tonic, label="tonic")
        plt.plot(y, [amplitude for _ in range(self.NR_DATA_POINTS)], label=f"total amplitude={round(amplitude, 3)}")
        plt.legend()
        plt.show()


class EDA_handler:
    eda_queue = deque(maxlen=121)
    counter = 0
    eda = EDA()

    # public function that empatica control flow can call to add a new data point
    def add_eda_point(self, datapoint):
        self.eda_queue.append(datapoint)

        # calculate measurements if 10 seconds has passed, and we have enough data points (30 seconds worth)
        if self.counter % 40 == 0 and len(self.eda_queue) == 121:
            amplitude, nr_peaks, auc = self.eda.calculate_measurements(list(self.eda_queue))
            # TODO use below line when we have found arousal and engagement
            # self._write_measurement_to_file(arousal, engagement)

        self.counter += 1

    def _write_measurement_to_file(self, arousal, engagement):
        # TODO write to measurement csv file
        pass



# TODO delete below when production ready
# how to use the eda classes
# - Send in data points when they are ready, using EDA_handler.add_eda_point()
# - every 10 seconds, new measurements will be derived for arousal and engagement
# does not require data points every 1/frequency seconds, however it requires data points in order
# if there is a corrupt data point, we need to interpolate it's value
if __name__ == "__main__":
    # READ DATA AND FORMAT
    data = pd.read_csv("S001/EDA.csv")
    # startTime = pd.to_datetime(float(data.columns.values[0]), unit="s")
    # sampleRate = float(data.iloc[0][0])
    data = data[data.index != 0]
    data.columns = ["EDA"]
    # data.index = pd.date_range(start=startTime, periods=len(data), freq='250L')

    # instantiate class
    eda_handler = EDA_handler()

    # add the first 161 data points, which is 40 seconds worth
    # after 30 seconds will create first measurement
    # after 10 more seconds (40 total) will create second measurement
    for d in data["EDA"][0:161]:
        eda_handler.add_eda_point(d)
