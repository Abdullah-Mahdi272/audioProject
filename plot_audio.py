import wave
import numpy as np
import matplotlib.pyplot as plt

file = 'wav_files/test.wav'
with wave.open(file, 'rb') as obj:
    n_channels = obj.getnchannels()
    if n_channels != 1:
        raise ValueError("This script only supports mono WAV files.")
    
    sample_freq = obj.getframerate()
    n_samples = obj.getnframes()
    signal_wave = obj.readframes(n_samples)
    sample_width = obj.getsampwidth()

t_audio = n_samples / sample_freq
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
times = np.linspace(0, t_audio, num=n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title('Mono Audio Signal')
plt.ylabel('Signal Wave')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()
