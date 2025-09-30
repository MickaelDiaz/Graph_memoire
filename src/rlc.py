import numpy as np
import matplotlib.pyplot as plt
import os

# Paramètres des composants
L = 1e-6     # Inductance en Henry (H)
C = 47e-6    # Capacité en Farad (F)
R_d = 0.364664590     # Résistance de damping en parallèle avec le condensateur (Ω)

# Vecteur fréquence (échelle logarithmique)
f = np.logspace(1, 6, 1000)  # De 10 Hz à 1 MHz
w = 2 * np.pi * f            # Pulsation rad/s

# Impédances individuelles
Z_L = 1j * w * L
Z_C = -1j / (w * C)
Z_Rd = R_d * np.ones_like(w)  # Résistance constante

# Association parallèle C // R_d
Y_C = 1 / Z_C
Y_Rd = 1 / Z_Rd
Y_C_total = Y_C + Y_Rd
Z_C_damped = 1 / Y_C_total  # Impédance équivalente C en parallèle avec R_d

# Impédance totale (L en série avec [C // R_d])
Z_total = (Z_L * Z_C_damped) / (Z_L + Z_C_damped)

# Module des impédances
Z_L_abs = np.abs(Z_L)
Z_C_abs = np.abs(Z_C)
Z_C_damped_abs = np.abs(Z_C_damped)
Z_total_abs = np.abs(Z_total)

# Fréquence de résonance
f_res = 1 / (2 * np.pi * np.sqrt(L * C))
f_con_res= 1 / (2* np.pi * R_d * C)

# Tracé des courbes
plt.figure(figsize=(10, 6))
plt.loglog(f, Z_L_abs, label="|Z_L| = ωL", linestyle="--", color="blue")
plt.loglog(f, Z_C_damped_abs, label="|Z_C_amortie| = C // R_d", linestyle="-.", color="orange")
plt.loglog(f, Z_total_abs, label="|Z_total| = Impédance équivalente", linewidth=2, color="red")

# Ligne verticale à la fréquence de résonance
plt.axvline(f_res, color="black", linestyle="--", label=f"f_LC = {f_res:.0f} Hz")
plt.axvline(f_con_res, color="black", linestyle=":", label=f"f_RC = {f_con_res:.0f} Hz")

# Personnalisation du graphique
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Impédance (Ω)")
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.legend()
plt.ylim(0, 550)  # Valeurs à ajuster selon ton cas
 # Valeurs à ajuster selon ton cas


# Sauvegarde
folder_path = "figures"
os.makedirs(folder_path, exist_ok=True)
file_name = "bypass_osci_damped.png"
output_path = os.path.join(folder_path, file_name)
plt.savefig(output_path, dpi=300)
plt.show()
