import numpy as np
import matplotlib.pyplot as plt
import os

# Paramètres de la tension d'entrée
V_rms = 20  # Tension efficace en volts (RMS)
V_max = V_rms * np.sqrt(2)  # Tension maximale (crête)
f = 50  # Fréquence de l'AC en Hz
t = np.linspace(0, 0.1, 1000)  # Plage de temps (sur 0.1 seconde pour voir plusieurs cycles)

# Signal alternatif d'entrée (sinusoïdal)
u_in = V_max * np.sin(2 * np.pi * f * t)

# Signal après redressement double alternance
u_out = np.abs(u_in)

# Tracer les courbes
plt.figure(figsize=(10, 6))

# Tracer la tension d'entrée (AC)
plt.plot(t, u_in, label="Tension d'entrée (AC)", color='blue', linestyle='--')

# Tracer la tension redressée (DC pulsée)
plt.plot(t, u_out, label="Tension redressée", color='red')

# Ajouter des détails au graphique
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.legend()
plt.grid(True)

folder_path = "figures"
file_name = "graphique_redressement.png"
output_path = os.path.join(folder_path, file_name)
plt.savefig(output_path, dpi=300)

# Afficher le graphique
plt.tight_layout()
plt.show()