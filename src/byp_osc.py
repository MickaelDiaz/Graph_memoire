import numpy as np
import matplotlib.pyplot as plt
import os

# Paramètres des composants
L = 1e-6  # Inductance en Henry (H)
C = 47e-6   # Capacité en Farad (F)
R_L = 10   # Résistance en parallèle pour modéliser les pertes

# Vecteur fréquence (échelle logarithmique)
f = np.logspace(1, 6, 1000)  # De 10 Hz à 1 MHz
w = 2 * np.pi * f  # Pulsation rad/s

# Impédances individuelles
Z_L = 1j * w * L
Z_C = -1j / (w * C)

# Impédance totale en parallèle (formule parallèle)
Z_total = (Z_L * Z_C) / (Z_L + Z_C)  # Ajout d'une résistance pour éviter une impédance infinie

# Module des impédances
Z_L_abs = np.abs(Z_L)
Z_C_abs = np.abs(Z_C)
Z_total_abs = np.abs(Z_total)

# Fréquence de résonance
f_res = 1 / (2 * np.pi * np.sqrt(L * C))

# Tracé des courbes
plt.figure(figsize=(10, 6))
plt.loglog(f, Z_L_abs, label="|Z_L| = ωL", linestyle="--", color="blue")
plt.loglog(f, Z_C_abs, label="|Z_C| = 1/(ωC)", linestyle=":", color="green")
plt.loglog(f, Z_total_abs, label="|Z_total| = Impédance équivalente", linewidth=2, color="red")

# Ligne verticale à la fréquence de résonance
plt.axvline(f_res, color="black", linestyle="--", label=f"f_LC = {f_res:.0f} Hz")

# Personnalisation du graphique
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Impédance (Ω)")
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.legend()
folder_path = "figures"
os.makedirs(folder_path, exist_ok=True)
file_name = "bypass_osci.png"
output_path = os.path.join(folder_path, file_name)
plt.savefig(output_path, dpi=300)
plt.show()
