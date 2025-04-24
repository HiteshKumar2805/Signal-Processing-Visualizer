import numpy as np

def generate_sine_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = np.sin(2 * np.pi * freq * t)
    return t, y

def generate_square_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = np.sign(np.sin(2 * np.pi * freq * t))
    return t, y

def generate_triangle_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = 2 * np.abs(2 * ((t * freq) % 1) - 1) - 1
    return t, y
