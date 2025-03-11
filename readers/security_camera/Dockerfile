FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY security_camera.py .

RUN pip install -r requirements.txt

CMD ["python", "security_camera.py"]