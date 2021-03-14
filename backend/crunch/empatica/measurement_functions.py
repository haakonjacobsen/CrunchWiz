import numpy as np
import statsmodels.api as sm


def compute_percentage_of_ibi_that_differ(list_of_ibi_values):
    # Percentage of successive IBI that differ by more than 50 ms."
    window_size = 10
    assert type(list_of_ibi_values) == list
    assert len(list_of_ibi_values) > window_size
    differs_more = 0
    differs_less = 0
    for i in range(1, window_size):
        if abs(list_of_ibi_values[i] - list_of_ibi_values[i - 1]) > 0.05:
            differs_more += 1
        else:
            differs_less += 1
    return differs_more / (differs_more + differs_less)


def compute_rmssd(list_of_ibi_values):
    """
    :param list_of_ibi_values:
    :return: Root mean square of successive differences (RMSSD)
    """
    window_size = 10
    assert list == type(list_of_ibi_values)
    assert len(list_of_ibi_values) > window_size
    total = 0
    for i in range(1, window_size):
        total += (list_of_ibi_values[i] - list_of_ibi_values[i - 1]) ** 2
    return (total / (window_size - 1)) ** 0.5


def compute_normal_ibi(list_of_ibi_values):
    """
    Removes IBI values that are too large or too small
    :param list_of_ibi_values:
    :return: list of normalized IBI values
    """
    min_ibi = 0.49  # Q: What is too short and too large?
    max_ibi = 0.52
    in_range_ibi_values = [ibi for ibi in list_of_ibi_values if min_ibi < ibi < max_ibi]
    #  Q: I have now removed "too short and too large" intervals. What do I do now?
    return in_range_ibi_values


def compute_emotional_regulation(list_of_ibi_values):
    """
    Computes emotional regulation based on a list of IBI values
    :param list_of_ibi_values:
    :return:
    """
    """
    mr K: "The root mean square of successive differences (RMSSD)
    ”normal” Inter-Beat Interval (IBI) à remove too short and too large
    intervals.
    Percentage of successive IBI that differ by more than 50 ms."

    I have interpreted this as 3 alternative ways, where I chose the last one. """
    rmssd = compute_rmssd(list_of_ibi_values)
    percentage_that_differ = compute_percentage_of_ibi_that_differ(list_of_ibi_values)
    normal = compute_normal_ibi(list_of_ibi_values)
    return (rmssd + percentage_that_differ + np.average(normal))/3


def compute_entertainment(list_of_hr_values):
    """
    This function only computes features that can be used as input to supervised learning.
    Currently outputs a placeholder value between 0 and 1.
    The average HRE
    The variance of the HR signal σ2
    The maximum HR max
    The minimum HR min
    The difference D between the maximum and the minimum HR
    The correlation coefficient R between HR recordings and the time t in which data were recorded
    This parameter provides a notion of the linearity of the signal (HR data) over time
    The autocorrelation ρ1 (lag equals 1) of the signal, which is used to detect the
    level of non-randomness in the HR data
    The approximate entropy (ApEnm,r)(Pincus 1991) of the signal which quantifies
    the unpredictability of fluctuations in the HR time series.
    """

    def ApEn(U, m, r) -> float:
        """
        Approximate_entropy. Source:
        https://en.wikipedia.org/wiki/Approximate_entropy
        """

        def _maxdist(x_i, x_j):
            return max([abs(ua - va) for ua, va in zip(x_i, x_j)])

        def _phi(m):
            x = [[U[j] for j in range(i, i + m - 1 + 1)] for i in range(N - m + 1)]
            C = [
                len([1 for x_j in x if _maxdist(x_i, x_j) <= r]) / (N - m + 1.0)
                for x_i in x
            ]
            return (N - m + 1.0) ** (-1) * sum(np.log(C))

        N = len(U)

        return abs(_phi(m + 1) - _phi(m))

    def normalize(value, min_range, max_range):
        return (value - min_range) / (max_range - min_range)

    list_of_hr_values = np.asarray(list_of_hr_values)
    avg_hr = np.average(list_of_hr_values)
    var_hr = np.var(list_of_hr_values)
    max_hr = np.amax(list_of_hr_values)
    min_hr = np.amin(list_of_hr_values)
    d = max_hr - min_hr
    p = np.corrcoef(list_of_hr_values, np.arange(len(list_of_hr_values)))
    p1 = sm.tsa.acf(list_of_hr_values, nlags=1, fft=False)
    approximate_entropy = ApEn(list_of_hr_values, 2, 3)

    return (normalize(avg_hr, 20, 200) + normalize(var_hr, 0, 1000) + normalize(max_hr, 20, 200)
            + normalize(min_hr, 20, 200) + normalize(d, 0, 180) + p1[0] + p1[1] + approximate_entropy + p[0][1]) / 8


def compute_stress(temps_list):
    """
    Predicts acute stress based on GSR temperature
    :param temps_list:
    :return: 1 if acute stress event found, 0.5 otherwise
    """
    temperature_sum = 0
    temperature_threshold = -0.02
    for i, temp in enumerate(temps_list[:-1]):
        change = temps_list[i+1] - temp
        if change > 0:
            temperature_sum = 0
            continue
        temperature_sum += change
        if temperature_sum < temperature_threshold:
            #  return abs(round(temperature_sum, 2))
            return 1
    return 0.5
