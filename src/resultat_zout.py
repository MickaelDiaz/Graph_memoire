import matplotlib.pyplot as plt
import os
# Fréquences en Hz
frequences = [20, 100, 500, 2000, 5000, 20000]

# Impédances de sortie (Zout) en milliohms pour chaque type d'alimentation
zout_lineaire_p16 = [83, 81, 80, 172, 398, 1344]
zout_lineaire_m16 = [150, 146, 139, 136, 134, 160]
zout_decoupage_p16 = [1886, 1765, 1729, 1704, 1690, 1689]
zout_decoupage_m16 = [10959, 2276, 583, 368, 507, 836]

# Création du graphe
plt.figure(figsize=(10, 6))

plt.plot(frequences, zout_decoupage_p16, marker='o', label='Découpage +16V')
plt.plot(frequences, zout_decoupage_m16, marker='o', label='Découpage -16V')
plt.plot(frequences, zout_lineaire_p16, marker='o', label='Linéaire +16V')
plt.plot(frequences, zout_lineaire_m16, marker='o', label='Linéaire -16V')


# Mise à l'échelle logarithmique de l'axe des fréquences
plt.xscale('log')
plt.xlabel('Fréquence (Hz)')
plt.ylabel("Impédance de sortie (mΩ)")
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend()
plt.tight_layout()

folder_path = "figures"
file_name = "z_out_lin.png"
output_path = os.path.join(folder_path, file_name)
plt.savefig(output_path, dpi=300)

plt.show()