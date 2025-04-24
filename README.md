# 🔍 SignalScope - Signal Processing Visualizer

SignalScope is a dynamic and interactive Streamlit-based web application designed to visualize and analyze signals in both time and frequency domains. It enables users, especially engineering students and enthusiasts, to explore concepts of signal generation, filtering, and sampling with real-time plots and audio capabilities.

---

## 🚀 Features

### 🎼 Signal Generation
- Generate **Sine**, **Square**, and **Triangle** waveforms.
- Customize **Frequency**, **Duration**, and **Sample Rate**.

### 📊 Time & Frequency Domain Analysis
- Real-time plots of signal in **Time Domain**.
- View frequency spectrum using **FFT** in **Frequency Domain**.

### 🧪 Digital Filter Application
- Apply **Low Pass**, **High Pass**, **Band Pass**, and **Band Stop** filters.
- Choose between **Butterworth** and **FIR** filter implementations.

### 🔁 Sampling Techniques
- Perform **Downsampling**, **Upsampling**, and **Interpolation**.
- Select interpolation method: `linear` or `zero-order hold`.

### 📤 WAV File Integration
- Upload and analyze `.wav` audio files.
- Playback audio directly in the app.

### 🎤 Microphone Input (optional)
- Record audio directly from your microphone (feature modularized, commented by default).

### 🔨 Prerequisites

Ensure you have the following installed:
- Python 3.8+
- pip

### 📦 Installation
```bash
git clone https://github.com/yourusername/SignalScope.git
cd SignalScope
pip install -r requirements.txt
```

## Running the app
```bash
-streamlit run app.py
````

## Technologies Used
### Python
- Streamlit - for frontend and interaction
- NumPy, SciPy - for signal processing
- Matplotlib - for plotting
- Soundfile/Scipy.io - for audio file handling

## Author
Hitesh Kumar S |
B.E. ECE | Panimalar Engineering College

## License 
This project is open-source and available under the MIT License.
