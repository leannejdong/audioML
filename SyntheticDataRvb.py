import numpy as np
import soundfile as sf
import librosa
from pydub import AudioSegment
from pydub.playback import play


# Set the parameters for the reverb
reverb_time = 2.0  # Reverb time in seconds
room_size = 30  # Size of the simulated room in meters

# Generate a clean audio signal
duration = 5.0  # Duration of the audio in seconds
sample_rate = 44100  # Sample rate of the audio
t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
clean_signal = np.sin(2 * np.pi * 440 * t)  # Generate a sinusoidal signal at 440Hz

# Generate an impulse response for the reverb
impulse_response = np.zeros(int(reverb_time * sample_rate))
impulse_response[0] = 1.0  # Generate an impulse

# Generate synthetic reverb by convolving the clean signal with the impulse response
reverb_signal = np.convolve(clean_signal, impulse_response)[:len(clean_signal)]

# Normalize the reverb signal
reverb_signal /= np.max(np.abs(reverb_signal))

# Save the audio signals to files
sf.write('clean_signal.wav', clean_signal, sample_rate)
sf.write('reverb_signal.wav', reverb_signal, sample_rate)

# Load and play the audio files using pydub
clean_audio = AudioSegment.from_wav('clean_signal.wav')
reverb_audio = AudioSegment.from_wav('reverb_signal.wav')

clean_audio.export('clean_signal.mp3', format='mp3')  # Export as MP3 for playback
reverb_audio.export('reverb_signal.mp3', format='mp3')

clean_audio.export('clean_signal.ogg', format='ogg')  # Export as OGG for playback
reverb_audio.export('reverb_signal.ogg', format='ogg')

# Play the audio files
play(clean_audio)
play(reverb_audio)