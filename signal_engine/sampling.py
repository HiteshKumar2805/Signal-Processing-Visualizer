# signal_engine/sampling.py

import numpy as np
from scipy.signal import resample

def downsample(signal, factor):
    return signal[::factor]

def upsample(signal, factor):
    upsampled = np.zeros(len(signal) * factor)
    upsampled[::factor] = signal
    return upsampled

def interpolate(signal, method="linear", factor=2):
    n = len(signal)
    x_old = np.arange(n)
    x_new = np.linspace(0, n - 1, n * factor)
    
    if method == "linear":
        return np.interp(x_new, x_old, signal)
    elif method == "zero-order":
        return np.repeat(signal, factor)
    else:
        raise ValueError("Interpolation method must be 'linear' or 'zero-order'")
