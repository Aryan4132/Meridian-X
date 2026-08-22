# Meridian-X backend sidecar container (used by docker-compose*.yml)
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        portaudio19-dev \
        libsndfile1 \
        curl \
    && rm -rf /var/lib/apt/lists/*

COPY meridian_backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY meridian_backend/ .

ENV MERIDIAN_DATA_DIR=/data
VOLUME ["/data"]

EXPOSE 4132

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD curl -fsS http://127.0.0.1:4132/api/health || exit 1

CMD ["python", "-m", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "4132"]
