import streamlit as st
from components.ui_controls import signal_controls, filter_controls
from components.signal_plotter import plot_time_domain, plot_frequency_domain
from signal_engine import generator, filters, sampling
from services.audio_converter import load_wav
# from services.microphone import record_audio  # Optional mic integration

#  Streamlit Config
st.set_page_config(page_title="SignalScope", layout="centered")
st.title("🔍 SignalScope - Signal Processing Visualizer")

#  Signal Controls
st.sidebar.header("📡 Signal Controls")
wave_type = st.sidebar.selectbox("Select Signal Type", ["Sine", "Square", "Triangle"])
freq = st.sidebar.slider("Frequency (Hz)", 1, 1000, 100)
duration = st.sidebar.slider("Duration (s)", 1, 5, 2)
sample_rate = st.sidebar.slider("Sample Rate (Hz)", 1000, 10000, 5000, step=100)

#  Signal Generation
if wave_type == "Sine":
    t, signal = generator.generate_sine_wave(freq, duration, sample_rate)
elif wave_type == "Square":
    t, signal = generator.generate_square_wave(freq, duration, sample_rate)
elif wave_type == "Triangle":
    t, signal = generator.generate_triangle_wave(freq, duration, sample_rate)

#  Visualize Raw Signal
st.subheader("📊 Time Domain")
plot_time_domain(t, signal, f"{wave_type} Wave")

st.subheader("🌐 Frequency Domain")
plot_frequency_domain(signal, sample_rate, f"{wave_type} Wave Spectrum")

#  Filter Controls
st.sidebar.header("🧪 Filter Configuration")
filter_type, implementation, cutoff_low, cutoff_high = filter_controls()

nyquist = 0.5 * sample_rate
valid_cutoff = True

# Validate cutoffs before applying filters
if filter_type != "None":
    if cutoff_low >= nyquist or (filter_type in ["Band Pass", "Band Stop"] and cutoff_high >= nyquist):
        st.error(f"⚠️ Cutoff frequencies must be less than Nyquist Frequency ({nyquist} Hz). Please adjust your values.")
        valid_cutoff = False

    if valid_cutoff:
        try:
            if implementation == "Butterworth":
                if filter_type == "Low Pass":
                    signal = filters.butter_filter(signal, cutoff_low, sample_rate, 'low')
                elif filter_type == "High Pass":
                    signal = filters.butter_filter(signal, cutoff_low, sample_rate, 'high')
                elif filter_type == "Band Pass":
                    signal = filters.bandpass_filter(signal, cutoff_low, cutoff_high, sample_rate)
                elif filter_type == "Band Stop":
                    signal = filters.bandstop_filter(signal, cutoff_low, cutoff_high, sample_rate)
            elif implementation == "FIR":
                btype = filter_type.lower().replace(" ", "")
                signal = filters.fir_filter(signal, cutoff_low, sample_rate, btype=btype)

            # Filtered signal plots
            st.markdown("## 🧹 Filtered Signal")
            plot_time_domain(range(len(signal)), signal, "Filtered Signal - Time Domain")
            plot_frequency_domain(signal, sample_rate, "Filtered Signal - Frequency Domain")

        except ValueError as ve:
            st.error(f"🚫 Filter Error: {ve}")

# WAV File Upload
st.sidebar.header("📤 Upload & Playback")
uploaded_file = st.sidebar.file_uploader("Upload WAV File", type=["wav"])
if uploaded_file:
    st.success("✅ Audio file uploaded!")
    sample_rate, signal = load_wav(uploaded_file)
    st.audio(uploaded_file, format="audio/wav")
    st.markdown("## 🔍 Uploaded Signal Analysis")
    plot_time_domain(range(len(signal)), signal, "Uploaded Signal - Time Domain")
    plot_frequency_domain(signal, sample_rate, "Uploaded Signal - Frequency Domain")

#  Sampling Options
st.sidebar.header("🔁 Sampling Options")
sampling_method = st.sidebar.selectbox("Sampling Method", ["None", "Downsample", "Upsample", "Interpolate"])
sampling_factor = st.sidebar.slider("Sampling Factor", 1, 10, 2)

if sampling_method == "Downsample":
    signal = sampling.downsample(signal, sampling_factor)
elif sampling_method == "Upsample":
    signal = sampling.upsample(signal, sampling_factor)
elif sampling_method == "Interpolate":
    interp_method = st.sidebar.selectbox("Interpolation Type", ["linear", "zero-order"])
    signal = sampling.interpolate(signal, method=interp_method, factor=sampling_factor)

if sampling_method != "None":
    st.markdown("## 🧬 Sampled Signal")
    plot_time_domain(range(len(signal)), signal, f"{sampling_method}d Signal - Time Domain")
    plot_frequency_domain(signal, sample_rate, f"{sampling_method}d Signal - Frequency Domain")

#  Microphone Recording (Optional Feature)
# st.sidebar.button("🎙️ Record from Microphone"):
#     with st.spinner("Recording..."):
#         sample_rate, signal = record_audio()
#     st.success("🎧 Recording Complete!")
#     st.audio(signal, format="audio/wav")
#     plot_time_domain(range(len(signal)), signal, "Recorded Signal - Time Domain")
#     plot_frequency_domain(signal, sample_rate, "Recorded Signal - Frequency Domain")
