FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY power_consumption.py .

RUN pip install -r requirements.txt

CMD ["python", "power_consumption.py"]