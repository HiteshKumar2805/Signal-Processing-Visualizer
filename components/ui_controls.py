# components/ui_controls.py

import streamlit as st

def signal_controls():
    st.sidebar.markdown("### ⚙️ Signal Configuration")
    
    signal_type = st.sidebar.selectbox("Select Signal Type", ["Sine", "Square", "Triangle", "Custom"])

    freq = st.sidebar.slider("Frequency (Hz)", 1, 1000, 440)
    duration = st.sidebar.slider("Duration (seconds)", 1, 5, 2)
    sample_rate = st.sidebar.slider("Sample Rate (Hz)", 1000, 16000, 8000)

    return signal_type, freq, duration, sample_rate


def filter_controls():
    st.sidebar.markdown("### 🧹 Filter Configuration")

    filter_type = st.sidebar.selectbox("Filter Type", ["None", "Low Pass", "High Pass", "Band Pass", "Band Stop"])
    implementation = st.sidebar.selectbox("Implementation", ["Butterworth", "FIR"])

    cutoff_low = cutoff_high = None

    if filter_type in ["Low Pass", "High Pass"]:
        cutoff_low = st.sidebar.slider("Cutoff Frequency (Hz)", 10, 4000, 1000)
    elif filter_type in ["Band Pass", "Band Stop"]:
        cutoff_low, cutoff_high = st.sidebar.slider("Cutoff Frequencies (Hz)", 10, 4000, (500, 1500))

    return filter_type, implementation, cutoff_low, cutoff_high
