import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_time_domain(t, y, title="Time Domain Signal"):
    fig, ax = plt.subplots()
    ax.plot(t, y)
    ax.set_title(title)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.grid(True)
    st.pyplot(fig)

def plot_frequency_domain(signal, sample_rate, title="Frequency Domain Spectrum"):
    N = len(signal)
    f = np.fft.fftfreq(N, d=1/sample_rate)
    Y = np.fft.fft(signal)
    
    # Keep only positive frequencies
    idx = np.where(f >= 0)
    f = f[idx]
    Y = np.abs(Y[idx]) * 2 / N

    fig, ax = plt.subplots()
    ax.plot(f, Y)
    ax.set_title(title)
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Magnitude")
    ax.grid(True)
    st.pyplot(fig)
