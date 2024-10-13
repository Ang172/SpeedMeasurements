# Progrma de Medición de Velocidad de Internet

Este proyecto mide la velocidad de tu conexión a Internet utilizando la librería `speedtest-cli`. Los resultados de cada medición (descarga, subida y ping) se guardan en un archivo CSV.

## Requisitos Previos

Antes de ejecutar este proyecto, necesitas tener instalado Python 3 y `pip` en tu sistema. También necesitarás las siguientes dependencias:

matplotlib==3.8.3
numpy==1.26.4
pandas==2.2.2
speedtest-cli==2.1.3

Que se encuentran en el archivo requirements.txt, para instalarlas ejecuta:

- pip install -r requirements.txt

## Setup y Ejecucion

Sigue los pasos a continuación para instalar las dependencias y ejecutar el proyecto:

1. Descomprime la carpeta en un directorio.

2. En el CLI posicionate en el directorio y ejecuta ServerUp.py con 

- python3 ServerUp.py

  esto te dara una lista con todos los servidores.

3. En el archivo Main.py edita del id del servidor que quieras ocupar (esta en la linea #7) y ejecuta con

- python3 Main.py

  este archivo va a recojer todos los datos de las mediciones cada 5 min y lo guarda en el archivo speed measurements.csv

4. Una vez ya tengas las mediciones termina el Main.py con Ctrl + z y ejecuta la MakeGraph.py con

- python3 MakeGraph.py

Y listo!!
