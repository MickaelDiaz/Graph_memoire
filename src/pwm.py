import numpy as np
import matplotlib.pyplot as plt
import os

# Paramètres du signal
fs = 10000  # Fréquence d'échantillonnage (Hz)
f_tri = 300  # Fréquence du signal triangulaire (Hz)
duration = 0.05  # Augmentation de la durée de la simulation (s)

# Génération du temps
t = np.linspace(0, duration, int(fs * duration))

# Génération du signal triangulaire
tri_wave = 1 - 2 * np.abs((t * f_tri) % 1 - 0.5)  # Normalisé entre -1 et 1

# Signal de sortie continue de la SMPS (tension de référence)
Vout = 0.3 + 0.2 * np.sin(2 * np.pi * 50 * t)  # Simulant des variations lentes

# Génération du signal PWM
pwm_signal = np.where(Vout < tri_wave, 1, 0)

# Création des subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 5), sharex=True)

# Premier subplot : signal triangulaire et tension de sortie
axs[0].plot(t, tri_wave, label='Signal triangulaire', linestyle='dashed')
axs[0].plot(t, Vout, label='Signal erreur : v_out - v_ref', linewidth=2)
axs[0].set_ylabel('Amplitude')
axs[0].legend()
axs[0].grid()

# Deuxième subplot : signal PWM
axs[1].step(t, pwm_signal, label='Signal MLI', where='mid', color='red')
axs[1].set_xlabel('Temps (s)')
axs[1].set_ylabel('Amplitude')
axs[1].legend()
axs[1].grid()

folder_path = "figures"
file_name = "pwm.png"
output_path = os.path.join(folder_path, file_name)
plt.savefig(output_path, dpi=300)

# Ajustement de l'affichage
plt.xlim(0, 0.05)
plt.tight_layout()

# Affichage
plt.show()