FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

COPY src/ ./src/

ENV PYTHONUNBUFFERED=1

CMD ["python3", "src/app.py"]
