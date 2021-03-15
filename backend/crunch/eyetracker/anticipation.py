class eyetracker:
    """The eyetracker class calculates various measurements based on the saccade and fixations"""

    # data points
    vals = []

    avg_speed = 0
    variance = 0

    "Appends new data points and checks if there is enough data to compute measurements"

    def updateVals(self, vals):
        enough_vals = -1
        for i in range(len(vals)):
            self.vals.append(vals[i])
        if len(self.vals) > 4:
            enough_vals = 1
        return enough_vals

    def saccade_duration(self, start_time2, end_time1):
        return start_time2 - end_time1

    def saccade_length(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def print_variance(self):
        print(self.variance)

    def average_speed(self):
        count = 0
        speed_sum = 0
        for i in range(1, len(self.vals)):
            sacc_dur = self.saccade_duration(self.vals[i][1], self.vals[i - 1][2])
            sacc_len = self.saccade_length(
                self.vals[i - 1][5],
                self.vals[i - 1][6],
                self.vals[i][5],
                self.vals[i][6],
            )
            sacc_speed = sacc_len / sacc_dur
            speed_sum += sacc_speed
            count += 1
        self.avg_speed = speed_sum / count

    def variance(self):
        sum_square_difference = 0
        count = 0
        for i in range(1, len(self.vals)):
            sacc_dur = self.saccade_duration(self.vals[i][1], self.vals[i - 1][2])
            sacc_len = self.saccade_length(
                self.vals[i - 1][5],
                self.vals[i - 1][6],
                self.vals[i][5],
                self.vals[i][6],
            )
            sacc_speed = sacc_len / sacc_dur
            sum_square_difference += (sacc_speed - self.avg_speed) ** 2
            count += 1
        self.variance = sum_square_difference / (count - 1)

    def compute_perceived_difficulty(self):
        count = 0
        sum = 0
        for i in range(1, len(self.vals)):
            sacc_dur = self.saccade_duration(self.vals[i][1], self.vals[i - 1][2])
            sacc_len = self.saccade_length(
                self.vals[i - 1][5],
                self.vals[i - 1][6],
                self.vals[i][5],
                self.vals[i][6],
            )
            pd = 1 / (1 + (sacc_len / sacc_dur))
            count += 1
            sum += pd
        return sum / count

    def compute_anticipation(self):
        self.average_speed()
        self.variance()
        count = 0
        sum_cube_difference = 0
        for i in range(1, len(self.vals)):
            sacc_dur = self.saccade_duration(self.vals[i][1], self.vals[i - 1][2])
            sacc_len = self.saccade_length(
                self.vals[i - 1][5],
                self.vals[i - 1][6],
                self.vals[i][5],
                self.vals[i][6],
            )
            sacc_speed = sacc_len / sacc_dur
            sum_cube_difference += (sacc_speed - self.avg_speed) ** 3
            count += 1
        return sum_cube_difference / ((count - 1) * (self.variance ** 0.5) ** 3)

    def compute_measurements(self, vals):
        if self.updateVals(vals) == 1:
            result = (self.compute_anticipation(), self.compute_perceived_difficulty())
            self.vals = []
            return result
