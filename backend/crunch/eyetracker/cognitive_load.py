import math
import pywt
import numpy as np
def lhipa(d):
    # find max decomposition level
    w = pywt.Wavelet('sym16')
    maxlevel = \
        pywt.dwt_max_level(len(d), filter_len = w.dec_len)
    # set high and low frequency band indeces
    hif, lof = 1, int(maxlevel / 2)

    # get detail coefficients of pupil diameter signal d
    cD_H = pywt.downcoef('d', d, 'sym16', 'per', level=hif)
    cD_L = pywt.downcoef ('d', d, 'sym16', 'per',level=lof)

    # normalize by 1/ 2j
    cD_H[:] = [x / math.sqrt (2** hif) for x in cD_H]
    cD_L[:] = [x / math.sqrt (2** lof) for x in cD_L]

    # obtain the LH:HF ratio
    cD_LH = cD_L
    for i in range(len(cD_L)):
        cD_LH[i] = cD_L[i] / cD_H [((2** lof )/(2** hif ))*i]

    # detect modulus maxima , see Duchowski et al. [15]
    cD_LHm = modmax(cD_LH)

    # threshold using universal threshold λuniv = σˆ (2logn)
    # where σˆ is the standard deviation of the noise
    λuniv = \
        np.std(cD_LHm) * math.sqrt (2.0 * np.log2(len(cD_LHm)))
    cD_LHt = pywt.threshold(cD_LHm, λuniv, mode="less")

    # get signal duration (in seconds)
    tt = d[-1].timestamp() - d[0].timestamp()

    # compute LHIPA
    ctr = 0
    for i in xrange(len(cD_LHt )):
        if math.fabs(cD_LHt[i]) > 0: ctr += 1
    LHIPA = float(ctr)/tt

    return LHIPA

print(lhipa([3.572,3.548,3.5175,3.60428,3.676]))
