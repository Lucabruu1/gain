import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import io

# === Funzioni ===
def apply_gain(audio_data, gain):
    """Applica guadagno al segnale audio."""
    return audio_data * gain

def plot_audio(audio_data, sample_rate, title="Audio Waveform"):
    """Crea un grafico del segnale audio."""
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(np.arange(len(audio_data)) / sample_rate, audio_data)
    ax.set_xlabel("Tempo [s]")
    ax.set_ylabel("Ampiezza")
    ax.set_title(title)
    ax.grid(True)
    return fig

def save_audio(audio_data, sample_rate):
    """Salva il file audio in memoria e restituisce i byte."""
    buffer = io.BytesIO()
    wavfile.write(buffer, sample_rate, audio_data.astype(np.int16))
    return buffer.getvalue()

# === Interfaccia Streamlit ===
st.title("🎧 Audio Amplifier")

uploaded_file = st.file_uploader("Carica un file WAV", type=["wav"])

if uploaded_file:
    try:
        sample_rate, data = wavfile.read(uploaded_file)

        if data.ndim > 1:
            data = data[:, 0]  # Converte in mono se stereo

        st.audio(uploaded_file, format="audio/wav", start_time=0)

        gain = st.slider("Gain:", 0.0, 2.0, 1.0, 0.1)

        amplified_data = apply_gain(data, gain)
        fig = plot_audio(amplified_data, sample_rate, title=f"Waveform (Gain {gain:.2f})")
        st.pyplot(fig)

        output_audio = save_audio(amplified_data, sample_rate)
        st.audio(output_audio, format="audio/wav")

        st.download_button(
            "⬇️ Scarica l'audio amplificato",
            data=output_audio,
            file_name=f"amplified_{gain:.2f}_audio.wav",
            mime="audio/wav"
        )

    except Exception as e:
        st.error(f"Errore durante l'elaborazione del file: {e}")

else:
    st.info("Carica un file WAV per iniziare.")