FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y libpq-dev gcc netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/scripts/entrypoint.sh

ENTRYPOINT ["/app/scripts/entrypoint.sh"]
