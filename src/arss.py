import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import os

# Paramètres
f_min = 50  # Fréquence minimale
f_max = 150  # Fréquence maximale
duration = 0.05  # Durée totale du signal
sampling_rate = 10000  # Fréquence d'échantillonnage
num_levels = 16  # Nombre de niveaux de quantification

# Vecteur temps
t = np.linspace(0, duration, int(sampling_rate * duration))

# Initialisation du signal
time_index = 0
tri_wave = []
freq = np.random.uniform(f_min, f_max)  # Première fréquence aléatoire

while time_index < len(t):
    T = 1 / freq

    t_period = np.linspace(0, T, int(sampling_rate * T), endpoint=False)
    tri_period = 0.5 + 0.5*signal.sawtooth(2 * np.pi * (1/T) * t_period, 0.5)
    
    # Quantification en amplitude (discrétisation par paliers)
    tri_period = np.round(tri_period * num_levels) / num_levels

    # Ajouter cette période au signal global
    tri_wave.extend(tri_period)
    
    # Mise à jour du compteur de temps
    time_index += len(t_period)
    
    # Nouvelle fréquence aléatoire après chaque descente
    freq = np.random.uniform(f_min, f_max)

# Tronquer si dépassement
tri_wave = np.array(tri_wave[:len(t)])

# Affichage du signal
plt.figure(figsize=(10, 5))
plt.plot(t, tri_wave, drawstyle='steps-post', label="Fréquence de découpage modulée aléatoirement dans le temps")
plt.grid(True)
plt.xlabel("Temps")
plt.ylabel("Fréquence de découpage")
plt.gca().get_yaxis().set_ticks([])
plt.gca().get_xaxis().set_ticks([])
plt.legend()

# Sauvegarde de l'image
folder_path = "figures"
os.makedirs(folder_path, exist_ok=True)
file_name = "arss.png"
output_path = os.path.join(folder_path, file_name)
plt.savefig(output_path, dpi=300)
plt.show()