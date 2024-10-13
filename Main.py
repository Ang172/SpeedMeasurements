import csv
import time
import speedtest
from datetime import datetime
import os

csv_file = "speed measurements.csv"

server_id = 51218

def medir_velocidad():
    st = speedtest.Speedtest(secure=True)

    st.get_servers([server_id])
    st.get_best_server()

    download_speed = round(st.download() / 1_000_000, 2)
    upload_speed = round(st.upload() / 1_000_000, 2)
    ping = round(st.results.ping, 2)
    return download_speed, upload_speed, ping

def guardar_en_csv(download_speed, upload_speed, ping):
    
    tiempo_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tiempo_actual, download_speed, upload_speed, ping])

if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Fecha y Hora", "Velocidad de Descarga (Mbps)", "Velocidad de Subida (Mbps)", "Ping (ms)"])

while True:
    try:
        download_speed, upload_speed, ping = medir_velocidad()
        guardar_en_csv(download_speed, upload_speed, ping)
        print(f"Medición guardada: {datetime.now()}")
        
        time.sleep(60*10)
    except Exception as e:
        print(f"Error: {e}")
