# importing the required module
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# I. Defining signal

time = np.arange(0, 100, 0.1)
output_path = os.path.abspath('Output_file/')
input_path = os.path.abspath('Input_file/stellar_spectrum.csv')
df = pd.read_csv(input_path, header=None, low_memory=False)
data = df.drop(df.index[:1])
print(df)
wave = data[data.columns[0]]
flux = data[data.columns[1]]
wave = wave.astype(float)
flux = flux.astype(float)
frames = [wave, flux]
spectrum = pd.concat(frames, axis=1, join='inner')
print(spectrum)

spectrum.plot()
plt.xlabel("Wavelength")
plt.ylabel("Flux")
plt.savefig(os.path.join(output_path, "spectrum.png"))
plt.close()
#
#
# # II. Normalizing the spectrum and making Signal to Noize Ratio
mean_norm = np.mean(flux)
std = 4500
SNR = mean_norm / std
plt.plot(spectrum)
plt.xlim([5550, 5560])
plt.savefig(output_path + "spectrum_normalized.png")
plt.close()
print("SNR is", SNR)


# III. Adding noise to signal
def white_noise(pure_spectrum, deviation, mu=0):
    return np.random.normal(mu, deviation, size=pure_spectrum.shape)

print(list(df.columns))

for x in range(0, 10):
    noise = white_noise(flux, std)
    flux_with_noise = flux + noise
    noise_image = pd.Series(noise)
    flux_with_noise_image = pd.Series(flux_with_noise)
    plt.xlim([5550, 5560])
    plt.plot(wave, flux, linewidth=.2)
    plt.plot(wave, flux_with_noise, linewidth=.2)
    frame = [wave, flux_with_noise_image]
    spectrum_noise_image = pd.concat(frame, axis=1, join='inner')
    np.savetxt(os.path.join(output_path, f"noised_spectra_data{x}.dat"), spectrum_noise_image.values)
    plt.savefig(os.path.join(output_path, f"noised_spectra{x}.png"), dpi=300)
plt.close()
plt.plot(spectrum_noise_image, linewidth=.2)
plt.savefig(os.path.join(output_path, "noise.png"))
#
#
