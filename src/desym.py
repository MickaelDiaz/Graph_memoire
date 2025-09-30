import numpy as np
import matplotlib.pyplot as plt
import os

# Paramètres
amp = 1
freq = 50
duration = 0.1
t = np.linspace(0, duration, 1000)
num_pulses = 50  # Nombre d'impulsions
t_min = 1e-3  
t_max = 5e-3

# Signaux s1 et s2
s1 = amp * np.sin(2 * np.pi * freq * t)
s2 = amp * np.sin(2 * np.pi * freq * t + np.pi)

# Fonction pour générer des impulsions triangulaires aléatoires sur toute la durée
def generate_triangle_pulses(t_min, t_max, num_pulses, duration):
    bruit = np.zeros_like(t)

    for _ in range(num_pulses):
        # Positionner le début de l'impulsion à des intervalles réguliers dans la durée
        start_time = np.random.uniform(t_min, duration - 0.01)  # Début de l'impulsion, éviter de dépasser la durée
        width = np.random.uniform(0.005, 0.02)  # Largeur de l'impulsion (0.005 à 0.02 s)
        amplitude = np.random.uniform(-0.2, 0.2)  # Amplitude de l'impulsion

        # Créer l'impulsion triangulaire
        pulse_start = int(start_time * len(t) / duration)
        pulse_end = int((start_time + width) * len(t) / duration)

        # Générer l'impulsion triangulaire
        bruit[pulse_start:pulse_end] = amplitude * (1 - np.abs((t[pulse_start:pulse_end] - start_time) / width - 0.5) * 2)

    return bruit

# Génération du bruit
bruit = generate_triangle_pulses(t_min, t_max, num_pulses, duration)

# Ajouter le bruit aux signaux
s1_bruite = s1 + bruit
s2_bruite = s2 + bruit

# Soustraction pour observer la désymétrisation
s_desym = s1_bruite - s2_bruite

# Affichage des résultats
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, bruit, label='bruit')
plt.title("Bruit de mode commun")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.ylim(-1, 1)
plt.legend(loc='lower left')

plt.subplot(3, 1, 2)
plt.plot(t, s1_bruite, label='s1 avec bruit', color='r')
plt.plot(t, s2_bruite, label='s2 avec bruit', color='g')
plt.title("Signaux bruités s1 et s2")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.legend(loc='lower left')

plt.subplot(3, 1, 3)
plt.plot(t, s_desym, label='s1 - s2', color='purple')
plt.title("Signal désymétrisé")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.legend(loc='lower left')



plt.tight_layout()
folder_path = "figures"
file_name = "desym.png"
output_path = os.path.join(folder_path, file_name)
plt.savefig(output_path, dpi=300)
plt.show()
