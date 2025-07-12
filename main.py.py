# Impor pustaka yang diperlukan
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Membaca file audio WAV
sample_rate, data_audio = wavfile.read('test 1.wav')

# Jika audio stereo (2 channel), ambil hanya satu channel
if len(data_audio.shape) > 1:
    data_audio = data_audio[:, 0]

# Menerapkan FFT untuk mengubah ke domain frekuensi
fft_out = np.fft.fft(data_audio)

# Ambil magnitudo dari hasil FFT
fft_magnitude = np.abs(fft_out)

# Hanya ambil setengah pertama hasil FFT (karena simetri)
n = len(data_audio)
frequencies = np.fft.fftfreq(n, 1/sample_rate)[:n//2]
fft_magnitude = fft_magnitude[:n//2]

# Membuat grafik spektrum frekuensi
plt.plot(frequencies, fft_magnitude, color='blue')
plt.title('Spektrum Frekuensi Audio')
plt.xlabel('Frekuensi (Hz)')
plt.ylabel('Magnitudo')
plt.grid(True)
plt.show()