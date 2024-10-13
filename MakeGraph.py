import matplotlib.pyplot as plt
import pandas as pd

csv_file = "speed measurements.csv"

df = pd.read_csv(csv_file)

df['Fecha y Hora'] = pd.to_datetime(df['Fecha y Hora'])

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

axs[0].plot(df['Fecha y Hora'], df['Velocidad de Descarga (Mbps)'], label='Descarga', color='blue')
axs[0].set_title('Velocidad de Descarga (Mbps)')
axs[0].set_ylabel('Mbps')
axs[0].grid(True)

axs[1].plot(df['Fecha y Hora'], df['Velocidad de Subida (Mbps)'], label='Subida', color='green')
axs[1].set_title('Velocidad de Subida (Mbps)')
axs[1].set_ylabel('Mbps')
axs[1].grid(True)

axs[2].plot(df['Fecha y Hora'], df['Ping (ms)'], label='Ping', color='red')
axs[2].set_title('Ping (ms)')
axs[2].set_ylabel('ms')
axs[2].grid(True)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("mediciones.png")

plt.show()
