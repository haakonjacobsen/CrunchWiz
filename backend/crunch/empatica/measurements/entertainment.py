import numpy as np
import statsmodels.api as sm


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
