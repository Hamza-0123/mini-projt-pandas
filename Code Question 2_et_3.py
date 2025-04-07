import numpy as np
import matplotlib.pyplot as plt

# Paramètres de la sinusoïde
fs = 1000  # Fréquence d'échantillonnage en Hz
t = np.arange(0, 1, 1/fs)  # Temps de 0 à 1 seconde
f1 = 50  # Fréquence de la première sinusoïde en Hz
f2 = 120  # Fréquence de la deuxième sinusoïde en Hz

# Génération des données sinusoïdales
signal = 0.5 * np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Application de la Transformée de Fourier
freqs = np.fft.fftfreq(len(signal), 1/fs)
fft_values = np.fft.fft(signal)

# Affichage du spectre de fréquences
plt.figure(figsize=(12, 6))
plt.plot(freqs[:len(freqs)//2], np.abs(fft_values)[:len(fft_values)//2])
plt.title('Spectre de Fréquences')
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.xlim(0, 200)  # Limiter l'axe des X pour voir les fréquences pertinentes
plt.show()