import numpy as np
import matplotlib.pyplot as plt
import os
# Paramètres
Ton = 1        # Temps de montée
Toff = 1.2     # Temps de repos
Tdec = 0.8     # Temps de décroissance
A = 5          # Valeur max atteinte
B = 2   
C = 8       # Valeur de départ pour la nouvelle courbe
T = Ton + Toff # Période du signal

# Vecteur de temps
t = np.linspace(0, 4*T, 1000)  # 3 périodes pour voir le cycle plusieurs fois

# Création des signaux distincts
signal_croissance = np.zeros_like(t)
signal_decroissance = np.zeros_like(t)
signal_croissance2 = np.zeros_like(t)
signal_decroissance2 = np.zeros_like(t)

for i in range(len(t)):
    time_in_period = t[i] % T  # Temps dans la période actuelle
    
    # Signal de croissance classique
    if time_in_period < Ton:
        signal_croissance[i] = C * time_in_period / Ton  
    elif time_in_period < Ton + Tdec:
        signal_decroissance[i] = max(C * (1 - (time_in_period - Ton) / Tdec), 0)  # Limite à 0
    else:
        signal_croissance[i] = 0
        signal_decroissance[i] = 0
    
    # Nouvelle courbe de croissance partant de B jusqu'à A
    if time_in_period < Ton:
        signal_croissance2[i] = B + (A - B) * time_in_period / Ton  # Croissance de B à A
    else:
        signal_croissance2[i] = 0  # Repos à 0 après Ton

    # Nouvelle décroissance de A à B, mais nulle pendant Ton
    if time_in_period >= Ton and time_in_period < Ton + Toff:
        signal_decroissance2[i] = A - (A - B) * (time_in_period - Ton) / Toff  # Décroissance de A à B
    else:
        signal_decroissance2[i] = 0  # Repos à 0 pendant Ton

# Création des sous-graphiques
fig, axs = plt.subplots(2, 1, figsize=(12, 6))

# Premier sous-graphique : Croissance et décroissance
axs[0].plot(t, signal_croissance, label='Chargement', color='blue', linestyle='--')  # Pointillé pour croissance
axs[0].plot(t, signal_decroissance, label='Déchargement', color='red')
axs[0].set_title("Courant dans la bobine en mode discontinu (DCM)")
axs[0].set_ylabel("Amplitude")
axs[0].legend()
axs[0].set_xticks([])

# Ajouter les annotations et lignes pointillées pour Ton et Toff
for i in range(4):  # Pour 4 périodes visibles
    axs[0].axvline(i * T + Ton, color='black', linestyle='dotted', linewidth=1)
    axs[0].axvline(i * T + Ton + Toff, color='black', linestyle='dotted', linewidth=1)
    axs[0].text(i * T + Ton, -0.8, 'Toff', ha='center', color='black', fontsize=10)
    axs[0].text(i * T + Ton + Toff, -0.8, 'Ton', ha='center', color='black', fontsize=10)

axs[0].grid(True)

# Deuxième sous-graphique : Croissance de B à A et décroissance de A à B
axs[1].plot(t, signal_croissance2, label='Chargement', color='green', linestyle='--')  # Pointillé pour croissance de B à A
axs[1].plot(t, signal_decroissance2, label='Déchargement', color='purple')
axs[1].set_title("Courant dans la bobine en mode continu (CCM)")
axs[1].set_ylabel("Amplitude")
axs[1].legend()
axs[1].set_xticks([])

# Ajouter les annotations et lignes pointillées pour Ton et Toff
for i in range(4):  # Pour 4 périodes visibles
    axs[1].axvline(i * T + Ton, color='black', linestyle='dotted', linewidth=1)
    axs[1].axvline(i * T + Ton + Toff, color='black', linestyle='dotted', linewidth=1)
    axs[1].text(i * T + Ton, -0.8, 'Toff', ha='center', color='black', fontsize=10)
    axs[1].text(i * T + Ton + Toff, -0.8, 'Ton', ha='center', color='black', fontsize=10)

axs[1].grid(True)

y_min = min(np.min(signal_croissance), np.min(signal_decroissance), np.min(signal_croissance2), np.min(signal_decroissance2))
y_max = max(np.max(signal_croissance), np.max(signal_decroissance), np.max(signal_croissance2), np.max(signal_decroissance2))
axs[0].set_ylim(y_min, y_max)
axs[1].set_ylim(y_min, y_max)

folder_path = "figures"
file_name = "dcm_ccm.png"
output_path = os.path.join(folder_path, file_name)
plt.savefig(output_path, dpi=300)

plt.tight_layout()
plt.show()
