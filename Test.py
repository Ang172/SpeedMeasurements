import speedtest

st = speedtest.Speedtest()

st.get_best_server()

download_speed = st.download()

upload_speed = st.upload()

ping = st.results.ping

print(f"Velocidad de descarga: {download_speed / 1_000_000:.2f} Mbps")
print(f"Velocidad de subida: {upload_speed / 1_000_000:.2f} Mbps")
print(f"Ping: {ping} ms")