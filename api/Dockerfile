FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY api.py .

# REST-API
EXPOSE 8080:8080

RUN pip install -r requirements.txt

CMD ["python", "api.py"]