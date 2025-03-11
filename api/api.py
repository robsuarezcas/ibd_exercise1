import json
import os
import pika
import requests
import time

from datetime import datetime
from flask import Flask, jsonify, request, Response

# Esperamos la inicialización de otros procesos (además de depends-on en docker-compose)
time.sleep(20)

# RABBITMQ
rabbitmq_host = os.getenv('RABBITMQ_HOST')
rabbitmq_credentials = pika.PlainCredentials(os.getenv('RABBITMQ_USERNAME'),os.getenv('RABBITMQ_PASSWORD'))
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host,credentials=rabbitmq_credentials))

# Creamos los canales y queues a usar
channel_temperature_humidity = connection.channel()
channel_temperature_humidity.queue_declare(queue='temperature_humidity')

channel_occupancy = connection.channel()
channel_occupancy.queue_declare(queue='occupancy')

channel_power_consumption = connection.channel()
channel_power_consumption.queue_declare(queue='power_consumption')

channel_security_camera = connection.channel()
channel_security_camera.queue_declare(queue='security_camera')

# REST-API
app = Flask(__name__)

# Función que recibe la información de los sensores
@app.route('/sensors/<sensor>', methods=['POST'])
def receive_sensor_data(sensor):
    try:
        data = request.get_json()

        # Añadir fecha y tiempo como metadata
        data['date'] = datetime.now()

        if not data:
            return jsonify({'error': 'No JSON received'}), 400

        # RABBITMQ
        try:
            eval(f'channel_{origin}').basic_publish(exchange='',
                                routing_key=origin,
                                body=json.dumps(data))

            # Confimar recibimiento y enviado correctos
            return jsonify({'message': f'Data received from {sensor}', 'data': data}), 200

        except pika.exceptions.AMQPConnectionError as e:
            return jsonify({"message": "Error with RabbitMQ connection"}), 500
        except pika.exceptions.ChannelWrongStateError as e:
            return jsonify({"message": "Error with RabbitMQ channel"}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Función que recupera la información obtenida
@app.route('/retrieve/<sensor>', methods=['GET'])
def retrieve_sensor_info(sensor):
    try:
        data = request.get_json()

        # Añadir fecha y tiempo como metadata
        data['date'] = datetime.now()

        if not data:
            return jsonify({'error': 'No JSON received'}), 400

        # RABBITMQ
        try:
            eval(f'channel_{origin}').basic_publish(exchange='',
                                routing_key=origin,
                                body=json.dumps(data))

            # Confimar recibimiento y enviado correctos
            return jsonify({'message': f'Data received from {sensor}', 'data': data}), 200

        except pika.exceptions.AMQPConnectionError as e:
            return jsonify({"message": "Error with RabbitMQ connection"}), 500
        except pika.exceptions.ChannelWrongStateError as e:
            return jsonify({"message": "Error with RabbitMQ channel"}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Usamos el modo debug para poder comprobar el correcto funcionamiento de los sensores
    app.run(host='0.0.0.0', port=8080, debug=True)
