import math

import numpy as np
import pywt


def compute_cognitive_load(lpup, rpup):
    """
    Computes the cognitive load based on the size of the pupils in a time window
    The modmax and lhipa algorithm are taken directly from this paper: https://doi.org/10.1145/3313831.3376394

    :param lpup: values for left pupil size
    :type lpup: list of int
    :param rpup: values for right pupil size
    :type rpup: list of int
    :return: Measure of cognitive load
    :rtype: float
    """
    assert len(lpup) == len(rpup)
    signal_dur = len(lpup) / 120
    average_pupil_values = [(l + r) / 2 for l, r in zip(lpup, rpup)]

    return lhipa(average_pupil_values, signal_dur)


def modmax(d):
    # compute signal modulus
    m = [0.0] * len(d)
    for i in range(len(d)):
        m[i] = math.fabs(d[i])

    # if value is larger than both neighbours , and strictly
    # larger than either , then it is a local maximum
    t = [0.0] * len(d)
    for i in range(len(d)):
        ll = m[i - 1] if i >= 1 else m[i]
        oo = m[i]
        rr = m[i + 1] if i < len(d) - 2 else m[i]
        if (ll <= oo and oo >= rr) and (ll < oo or oo > rr):
            # compute magnitude
            t[i] = math.sqrt(d[i] ** 2)
        else:
            t[i] = 0.0
    return t


def lhipa(d, signal_dur):
    # find max decomposition level
    w = pywt.Wavelet("sym16")
    maxlevel = pywt.dwt_max_level(len(d), filter_len=w.dec_len)
    # set high and low frequency band indeces
    hif, lof = 1, int(maxlevel / 2)
    print(hif)
    print(lof)

    # get detail coefficients of pupil diameter signal d
    cD_H = pywt.downcoef("d", d, "sym16", "per", level=hif)
    cD_L = pywt.downcoef("d", d, "sym16", "per", level=lof)

    # normalize by 1/ 2j
    cD_H[:] = [x / math.sqrt(2 ** hif) for x in cD_H]
    cD_L[:] = [x / math.sqrt(2 ** lof) for x in cD_L]

    # obtain the LH:HF ratio
    cD_LH = cD_L
    for i in range(len(cD_L)):
        cD_LH[i] = cD_L[i] / cD_H[((2 ** lof) // (2 ** hif)) * i]

    # detect modulus maxima , see Duchowski et al. [15]
    cD_LHm = modmax(cD_LH)

    # threshold using universal threshold λuniv = σˆ (2logn)
    # where σˆ is the standard deviation of the noise
    λuniv = np.std(cD_LHm) * math.sqrt(2.0 * np.log2(len(cD_LHm)))
    cD_LHt = pywt.threshold(cD_LHm, λuniv, mode="less")

    # get signal duration (in seconds)
    tt = signal_dur
    # compute LHIPA
    ctr = 0
    for i in range(len(cD_LHt)):
        if math.fabs(cD_LHt[i]) > 0:
            ctr += 1
    LHIPA = float(ctr) / tt

    return LHIPA
