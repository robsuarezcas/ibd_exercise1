import random
import requests
import time

# Esperamos la inicialización de otros procesos (además de depends-on en docker-compose)
time.sleep(25)

# Posibles localizaciones de cada sensor
zones = ['entrada', 'pasillo_1', 'pasillo_2', 'sala_comun', 'cafeteria', 'salida']

# Implementación REST API
url = 'http://api:8080/sensors/occupancy'
headers = {'Content-Type': 'application/json'}

while True:
   data = {
      'zone': random.choice(zones),
      'occupancy': random.randint(0, 50),
      'movement': random.choice([True, False]),
      'dwell_time': round(random.uniform(0.5, 15), 2)
   }
    
   response = requests.post(url, json=data, headers=headers)
   print('Response:', response.status_code, response.text)

   # Tiempo espera entre recolección de datos
   time.sleep(60)