import random
import requests
import time

# Esperamos la inicialización de otros procesos (además de depends-on en docker-compose)
time.sleep(25)

# Posibles valores de la calidad del aire
air_quality = ['baja', 'media', 'alta']

# Implementación REST API
url = 'http://api:8080/sensors/temperature_humidity'
headers = {'Content-Type': 'application/json'}

while True:
   data = {
      'temperature': round(random.uniform(20, 30), 2),
      'humidity': round(random.uniform(30, 60), 2),
      'air_quality': random.choice(air_quality)
   }
    
   response = requests.post(url, json=data, headers=headers)
   print('Response:', response.status_code, response.text)

   # Tiempo espera entre recolección de datos
   time.sleep(30)