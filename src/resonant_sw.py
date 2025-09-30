import numpy as np
import matplotlib.pyplot as plt
import os

def damped_oscillation(t, freq, damping_2, amplitude=0.2):
    return 0.7 * amplitude * np.exp(-damping_2 * 4*t) * np.cos(2 * np.pi * freq * t )

def damped_oscillation_1(t, freq, damping, amplitude=0.2):
    return 0.2 + 2* amplitude * np.exp(-damping * t) * np.cos(2 * np.pi * 0.16 * freq * t + np.pi)

def generate_waveform(t, period, oscillation_freq, damping):
    waveform = np.zeros_like(t)
    
    for i in range(len(t)):
        phase = (t[i] % period) / period
        time_in_period = t[i] % period  # Temps relatif dans la période

        if phase < 0.5:
            waveform[i] = 1  # Signal HIGH
            # Ajout d'oscillation au début du passage à 1
            if phase < 0.2:
                waveform[i] += damped_oscillation(time_in_period, oscillation_freq, damping)
            # Ajout d'oscillation juste avant de descendre à 0
            elif phase > 0.3:
                waveform[i] -= damped_oscillation_1(time_in_period - 0.28 * period, oscillation_freq, damping)
        else:
            waveform[i] = 0  # Signal LOW
    
    return waveform

# Paramètres du signal
T = 1e-3  # Période de l'onde (1 ms)
f_osc = 50e3  # Fréquence des oscillations parasites (50 kHz)
damping = 10000  # Facteur d'amortissement
damping_2 = 0

t = np.linspace(0,  2*T, 1000)  # Temps
waveform = generate_waveform(t, T, f_osc, damping)

# Affichage
plt.figure(figsize=(10, 4))
plt.plot(t * 1e3, waveform, label="Tension drain-source")  # Convertir en ms pour l'axe des X

# Affichage des transitions
plt.xlabel("Temps")
plt.ylabel("Amplitude")

# Ajouter une légende et une grille
plt.legend()

for i in range(2):  # Pour 4 périodes visible
    osc_1_pos = i * T * 1e3 + (T) * 1e3 - 0.4
    osc_2_pos = i * T * 1e3 + 0.26
    # Convertir les positions en millisecondes (en multipliant par 1e3)
    plt.axvline(i * T * 1e3 + (T / 2) * 1e3, color='black', linestyle='dotted', linewidth=1)  # Toff
    plt.axvline(i * T * 1e3 + T * 1e3, color='black', linestyle='dotted', linewidth=1)  # Ton
    
    # Placer les annotations sur l'axe des x en millisecondes
    plt.text(i * T * 1e3 + (T / 2) * 1e3, -0.13, 'Ton', ha='center', color='black', fontsize=10)  # Un peu au-dessus de l'axe y
    plt.text(i * T * 1e3 + T * 1e3, -0.13, 'Toff', ha='center', color='black', fontsize=10)  # Un peu au-dessus de l'axe y

    plt.text(osc_1_pos - 0.2, 0.4, "Oscillation 2", ha='center', color='red', fontsize=10, fontweight='bold')
    plt.text(osc_2_pos - 0.2, 0.7, "Oscillation 1", ha='center', color='blue', fontsize=10, fontweight='bold')
plt.xlim(0, 2)
plt.gca().axes.get_xaxis().set_visible(False)
plt.grid(True)

# Sauvegarde de l'image
folder_path = "figures"
file_name = "carre_osci.png"
output_path = os.path.join(folder_path, file_name)
plt.savefig(output_path, dpi=300)

# Afficher le graphique
plt.show()
