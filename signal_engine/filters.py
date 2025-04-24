from scipy.signal import butter, lfilter
from scipy.signal import firwin, lfilter

def butter_filter(signal, cutoff, sample_rate, btype='low', order=5):
    nyq = 0.5 * sample_rate
    normal_cutoff = cutoff / nyq
    if not (0 < normal_cutoff < 1):
        raise ValueError(f"Cutoff frequency must be between 0 and Nyquist ({nyq}) Hz. Got: {cutoff} Hz")
    b, a = butter(order, normal_cutoff, btype=btype, analog=False)
    return lfilter(b, a, signal)

def bandpass_filter(signal, lowcut, highcut, sample_rate, order=5):
    nyq = 0.5 * sample_rate
    low = lowcut / nyq
    high = highcut / nyq
    if not (0 < low < high < 1):
        raise ValueError(f"Bandpass cutoff range must be between 0 and Nyquist ({nyq}) Hz. Got: {lowcut}-{highcut} Hz")
    b, a = butter(order, [low, high], btype='band')
    return lfilter(b, a, signal)

def bandstop_filter(signal, lowcut, highcut, sample_rate, order=5):
    nyq = 0.5 * sample_rate
    low = lowcut / nyq
    high = highcut / nyq
    if not (0 < low < high < 1):
        raise ValueError(f"Bandstop cutoff range must be between 0 and Nyquist ({nyq}) Hz. Got: {lowcut}-{highcut} Hz")
    b, a = butter(order, [low, high], btype='bandstop')
    return lfilter(b, a, signal)

def fir_filter(signal, cutoff, sample_rate, btype='low', order=101):
    nyq = 0.5 * sample_rate
    normal_cutoff = cutoff / nyq
    if btype not in ['low', 'high']:
        raise ValueError("FIR supports only 'low' and 'high' filters.")
    if not (0 < normal_cutoff < 1):
        raise ValueError(f"Cutoff frequency must be between 0 and Nyquist ({nyq}) Hz. Got: {cutoff} Hz")
    b = firwin(order, normal_cutoff, pass_zero=(btype == 'low'))
    return lfilter(b, [1.0], signal)
