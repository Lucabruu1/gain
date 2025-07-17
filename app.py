# prompt: puoi esportarmelo per streamlit

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import io


# Function definitions (same as before)
def apply_gain(audio_data, gain):
    """Applies gain to the audio data."""
    return audio_data * gain

def plot_audio(audio_data, sample_rate, title="Audio Waveform"):
    """Plots the audio waveform."""
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(np.arange(len(audio_data)) / sample_rate, audio_data)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Amplitude")
    ax.set_title(title)
    ax.grid(True)
    return fig

def save_audio(audio_data, sample_rate):
    """Saves the audio data to a WAV file in memory and returns bytes."""
    buffer = io.BytesIO()
    wavfile.write(buffer, sample_rate, audio_data.astype(np.int16)) # Streamlit audio expects int16
    return buffer.getvalue()

st.title("Audio Amplifier")

# Upload the WAV file
uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file is not None:
    # Read the WAV file
    try:
        sample_rate, data = wavfile.read(uploaded_file)

        # Ensure data is mono (select the first channel if stereo)
        if data.ndim > 1:
            data = data[:, 0]

        st.audio(uploaded_file, format='audio/wav', start_time=0)

        # Create a slider for gain control
        gain = st.slider("Gain:", min_value=0.0, max_value=2.0, step=0.1, value=1.0)

        # Apply gain
        amplified_data = apply_gain(data, gain)

        # Plot the audio
        fig = plot_audio(amplified_data, sample_rate, title=f"Audio Waveform (Gain: {gain:.2f})")
        st.pyplot(fig)

        # Save and provide download link
        output_audio_bytes = save_audio(amplified_data, sample_rate)
        st.audio(output_audio_bytes, format='audio/wav')

        # Add a download button
        st.download_button(
            label="Download Amplified Audio",
            data=output_audio_bytes,
            file_name=f"amplified_{gain:.2f}_audio.wav",
            mime="audio/wav"
        )

    except Exception as e:
        st.error(f"Error processing file: {e}")

else:
    st.info("Please upload a WAV file to get started.")


# Function definitions (same as before)
def apply_gain(audio_data, gain):
    """Applies gain to the audio data."""
    return audio_data * gain

def plot_audio(audio_data, sample_rate, title="Audio Waveform"):
    """Plots the audio waveform."""
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(np.arange(len(audio_data)) / sample_rate, audio_data)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Amplitude")
    ax.set_title(title)
    ax.grid(True)
    return fig

def save_audio(audio_data, sample_rate):
    """Saves the audio data to a WAV file in memory and returns bytes."""
    buffer = io.BytesIO()
    wavfile.write(buffer, sample_rate, audio_data.astype(np.int16)) # Streamlit audio expects int16
    return buffer.getvalue()

st.title("Audio Amplifier")

# Upload the WAV file
uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file is not None:
    # Read the WAV file
    try:
        sample_rate, data = wavfile.read(uploaded_file)

        # Ensure data is mono (select the first channel if stereo)
        if data.ndim > 1:
            data = data[:, 0]

        st.audio(uploaded_file, format='audio/wav', start_time=0)

        # Create a slider for gain control
        gain = st.slider("Gain:", min_value=0.0, max_value=2.0, step=0.1, value=1.0)

        # Apply gain
        amplified_data = apply_gain(data, gain)

        # Plot the audio
        fig = plot_audio(amplified_data, sample_rate, title=f"Audio Waveform (Gain: {gain:.2f})")
        st.pyplot(fig)

        # Save and provide download link
        output_audio_bytes = save_audio(amplified_data, sample_rate)
        st.audio(output_audio_bytes, format='audio/wav')

        # Add a download button
        st.download_button(
            label="Download Amplified Audio",
            data=output_audio_bytes,
            file_name=f"amplified_{gain:.2f}_audio.wav",
            mime="audio/wav"
        )

    except Exception as e:
        st.error(f"Error processing file: {e}")

else:
    st.info("Please upload a WAV file to get started.")

# Function definitions (same as before)
def apply_gain(audio_data, gain):
    """Applies gain to the audio data."""
    return audio_data * gain

def plot_audio(audio_data, sample_rate, title="Audio Waveform"):
    """Plots the audio waveform."""
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(np.arange(len(audio_data)) / sample_rate, audio_data)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Amplitude")
    ax.set_title(title)
    ax.grid(True)
    return fig

def save_audio(audio_data, sample_rate):
    """Saves the audio data to a WAV file in memory and returns bytes."""
    buffer = io.BytesIO()
    wavfile.write(buffer, sample_rate, audio_data.astype(np.int16)) # Streamlit audio expects int16
    return buffer.getvalue()

st.title("Audio Amplifier")

# Upload the WAV file
uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file is not None:
    # Read the WAV file
    try:
        sample_rate, data = wavfile.read(uploaded_file)

        # Ensure data is mono (select the first channel if stereo)
        if data.ndim > 1:
            data = data[:, 0]

        st.audio(uploaded_file, format='audio/wav', start_time=0)

        # Create a slider for gain control
        gain = st.slider("Gain:", min_value=0.0, max_value=2.0, step=0.1, value=1.0)

        # Apply gain
        amplified_data = apply_gain(data, gain)

        # Plot the audio
        fig = plot_audio(amplified_data, sample_rate, title=f"Audio Waveform (Gain: {gain:.2f})")
        st.pyplot(fig)

        # Save and provide download link
        output_audio_bytes = save_audio(amplified_data, sample_rate)
        st.audio(output_audio_bytes, format='audio/wav')

        # Add a download button
        st.download_button(
            label="Download Amplified Audio",
            data=output_audio_bytes,
            file_name=f"amplified_{gain:.2f}_audio.wav",
            mime="audio/wav"
        )

    except Exception as e:
        st.error(f"Error processing file: {e}")

else:
    st.info("Please upload a WAV file to get started.")

# Function definitions (same as before)
def apply_gain(audio_data, gain):
    """Applies gain to the audio data."""
    return audio_data * gain

def plot_audio(audio_data, sample_rate, title="Audio Waveform"):
    """Plots the audio waveform."""
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(np.arange(len(audio_data)) / sample_rate, audio_data)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Amplitude")
    ax.set_title(title)
    ax.grid(True)
    return fig

def save_audio(audio_data, sample_rate):
    """Saves the audio data to a WAV file in memory and returns bytes."""
    buffer = io.BytesIO()
    wavfile.write(buffer, sample_rate, audio_data.astype(np.int16)) # Streamlit audio expects int16
    return buffer.getvalue()

st.title("Audio Amplifier")

# Upload the WAV file
uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file is not None:
    # Read the WAV file
    try:
        sample_rate, data = wavfile.read(uploaded_file)

        # Ensure data is mono (select the first channel if stereo)
        if data.ndim > 1:
            data = data[:, 0]

        st.audio(uploaded_file, format='audio/wav', start_time=0)

        # Create a slider for gain control
        gain = st.slider("Gain:", min_value=0.0, max_value=2.0, step=0.1, value=1.0)

        # Apply gain
        amplified_data = apply_gain(data, gain)

        # Plot the audio
        fig = plot_audio(amplified_data, sample_rate, title=f"Audio Waveform (Gain: {gain:.2f})")
        st.pyplot(fig)

        # Save and provide download link
        output_audio_bytes = save_audio(amplified_data, sample_rate)
        st.audio(output_audio_bytes, format='audio/wav')

        # Add a download button
        st.download_button(
            label="Download Amplified Audio",
            data=output_audio_bytes,
            file_name=f"amplified_{gain:.2f}_audio.wav",
            mime="audio/wav"
        )

    except Exception as e:
        st.error(f"Error processing file: {e}")

else:
    st.info("Please upload a WAV file to get started.")

# Function definitions (same as before)
def apply_gain(audio_data, gain):
    """Applies gain to the audio data."""
    return audio_data * gain

def plot_audio(audio_data, sample_rate, title="Audio Waveform"):
    """Plots the audio waveform."""
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(np.arange(len(audio_data)) / sample_rate, audio_data)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Amplitude")
    ax.set_title(title)
    ax.grid(True)
    return fig

def save_audio(audio_data, sample_rate):
    """Saves the audio data to a WAV file in memory and returns bytes."""
    buffer = io.BytesIO()
    wavfile.write(buffer, sample_rate, audio_data.astype(np.int16)) # Streamlit audio expects int16
    return buffer.getvalue()

st.title("Audio Amplifier")

# Upload the WAV file
uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file is not None:
    # Read the WAV file
    try:
        sample_rate, data = wavfile.read(uploaded_file)

        # Ensure data is mono (select the first channel if stereo)
        if data.ndim > 1:
            data = data[:, 0]

        st.audio(uploaded_file, format='audio/wav', start_time=0)

        # Create a slider for gain control
        gain = st.slider("Gain:", min_value=0.0, max_value=2.0, step=0.1, value=1.0)

        # Apply gain
        amplified_data = apply_gain(data, gain)

        # Plot the audio
        fig = plot_audio(amplified_data, sample_rate, title=f"Audio Waveform (Gain: {gain:.2f})")
        st.pyplot(fig)

        # Save and provide download link
        output_audio_bytes = save_audio(amplified_data, sample_rate)
        st.audio(output_audio_bytes, format='audio/wav')

        # Add a download button
        st.download_button(
            label="Download Amplified Audio",
            data=output_audio_bytes,
            file_name=f"amplified_{gain:.2f}_audio.wav",
            mime="audio/wav"
        )

    except Exception as e:
        st.error(f"Error processing file: {e}")

else:
    st.info("Please upload a WAV file to get started.")
