import random
import requests
import time

# Esperamos la inicialización de otros procesos (además de depends-on en docker-compose)
time.sleep(25)

# Implementación REST API
url = 'http://api:8080/sensors/power_consumption'
headers = {'Content-Type': 'application/json'}

while True:
   data = {
      'power_consumption': round(random.uniform(0.5, 5.0), 2),
      'voltage': round(random.uniform(210, 230), 2),
      'current': round(random.uniform(0.5, 10.0), 2),
      'power_factor': round(random.uniform(0.0, 1.0), 2)
   }
    
   response = requests.post(url, json=data, headers=headers)
   print('Response:', response.status_code, response.text)

   # Tiempo espera entre recolección de datos
   time.sleep(5)
