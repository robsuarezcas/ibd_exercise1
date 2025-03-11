FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY temperature_humidity.py .

RUN pip install -r requirements.txt

CMD ["python", "temperature_humidity.py"]