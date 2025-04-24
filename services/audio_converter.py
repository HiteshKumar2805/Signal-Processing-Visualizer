# services/audio_converter.py

import numpy as np
from scipy.io import wavfile
import sounddevice as sd

def load_wav(path):
    fs, data = wavfile.read(path)
    
    # Handle stereo by converting to mono
    if len(data.shape) == 2:
        data = data.mean(axis=1)

    # Normalize to -1.0 to 1.0
    if data.dtype != np.float32 and data.dtype != np.float64:
        data = data / np.max(np.abs(data))

    return fs, data

def record_audio(duration=3, fs=44100):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    print("Recording complete.")
    return fs, audio.flatten()
