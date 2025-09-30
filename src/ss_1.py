import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square
import os

freq = 6000
t = np.linspace(-2,2,1000)

sin_card = np.sinc(10*t)
sin_spread = np.sinc(2*t) * 0.6* square(2 * np.pi * 0.15 * t + np.pi/2) + 0.08 * np.sin(2 * np.pi * freq * t) 

plt.figure(figsize=(10, 5))
plt.plot(t,sin_card,label="Signal résiduel du découpage")
plt.plot(t,sin_spread,label="Signal résiduel du découpage étalé spectralement")
plt.grid(True)
plt.ylim((-0.5,1.25))
plt.ylabel("Amplitude")
# Mettre les ticks nuls, comme ça pas d'échelle
plt.gca().get_xaxis().set_ticks([])
plt.xticks([0], ["Fréquence de découpage"])

plt.axvspan(-0.5, 0.5, color='gray', alpha=0.3, label="Bande d'étalement fréquentielle")

# Ajouter un texte pour indiquer "Bande de Carson"
# plt.text(0, 1.1, "Bande d'étalement", horizontalalignment='center', verticalalignment='center', color='black',weight ="bold")
plt.legend(loc='lower left')

folder_path = "figures"
file_name = "spread_spectrum.png"
output_path = os.path.join(folder_path, file_name)
plt.savefig(output_path, dpi=300)

plt.show()