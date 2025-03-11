import random
import requests
import time

# Esperamos la inicialización de otros procesos (además de depends-on en docker-compose)
time.sleep(25)

# Posibles estados y alertas de la cámara
statuses = ["active", "inactive"]
alerts = ["motion detected", "unauthorized person", "abandoned object", "no alert"]
alert_levels = ["low", "medium", "high"]

# Implementación REST API
url = 'http://api:8080/sensors/security_camera'
headers = {'Content-Type': 'application/json'}

while True:
    data = {
        'status': random.choice(statuses),
        'alerts': random.choice(alerts),
        'alert_level': random.choice(alert_levels)
    }
    
    response = requests.post(url, json=data, headers=headers)
    print('Response:', response.status_code, response.text)

    # Tiempo espera entre recolección de datos
    time.sleep(120)

