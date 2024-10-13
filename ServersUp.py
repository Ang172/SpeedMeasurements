"""
ID: 58960 - INTERNEXA - Santiago - Chile
ID: 1858 - Entel - Santiago - Chile
ID: 21436 - Movistar Chile - Santiago - Chile
ID: 51218 - Mundo Chile - Santiago - Chile
ID: 29422 - wmax spa - Santiago - Chile
ID: 12732 - Orbyta S.A. - Santiago - Chile
ID: 8793 - Convergia Telecom S.A. - Santiago - Chile
ID: 53694 - Hostpit Cloud SpA - Santiago - Chile
ID: 58687 - Grupo GTD - Macul - Chile
ID: 8017 - Claro Chile - Santiago - Chile
"""
import speedtest

st = speedtest.Speedtest(secure = True)

servers = st.get_servers()

for server_list in servers.values():
    for server in server_list:
        print(f"ID: {server['id']} - {server['sponsor']} - {server['name']} - {server['country']}")
