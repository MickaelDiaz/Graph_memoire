import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.fftpack import fft, fftfreq

# --- Paramètres ---
fs = 40000               # Fréquence d'échantillonnage (Hz)
f_signal = 50            # Fréquence fondamentale du signal (Hz)
T = 1 / f_signal         # Période fondamentale
N = int(4 * T * fs)      # Nombre de points pour 4 périodes exactes
t = np.linspace(0, 4*T, N, endpoint=False)  # Temps sur 4 périodes
V_amplitude = 20         # Amplitude crête (par exemple, pour 230V RMS)
V_diode = 0.7            # Seuil de conduction des diodes (volts)

# --- Génération du signal sinusoïdal d'entrée ---
v_in = V_amplitude * np.sin(2 * np.pi * f_signal * t)

# --- Modèle de redressement double alternance avec seuil des diodes ---
def graetz_model(v):
    """ Applique un redressement double alternance avec seuil des diodes. """
    v_out = np.abs(v)      # Redressement de base
    v_out[v_out < V_diode] = 0  # Blocage des tensions sous le seuil
    return v_out

v_out = graetz_model(v_in)

# Pour observer les harmoniques, on soustrait la composante DC :
v_out_centered = v_out - np.mean(v_out)

# --- Analyse fréquentielle avec FFT ---
fft_values = fft(v_out_centered)        # Transformée de Fourier
frequencies = fftfreq(N, 1/fs)            # Fréquences associées

# --- Tracer le spectre fréquentiel ---
plt.figure(figsize=(12, 6))
plt.plot(frequencies[:N//2], np.abs(fft_values[:N//2]) / N, label="Spectre fréquentiel")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Tension (V)")
plt.xlim(0, 1000)
plt.grid(True)
plt.legend()

plt.xticks(np.arange(0, 1001, 100))

folder_path = "figures"
file_name = "disto_graetz.png"
output_path = os.path.join(folder_path, file_name)
plt.savefig(output_path, dpi=300)

plt.tight_layout()
plt.show()
