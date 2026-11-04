#
# 1. Build stage
#
FROM python:3.14-slim-bookworm AS builder

# Copiar los binarios de uv directamente desde la imagen oficial
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Paquetes de compilación para CFFI / WeasyPrint
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias del proyecto
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project --no-dev

#
# 2. Final stage
#
FROM python:3.14-slim-bookworm

WORKDIR /app

# Variables de entorno para Python y Flask
ENV PORT=8080 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# Dependencias de ejecución para WeasyPrint, fuentes y gráficos
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi8 \
    fonts-liberation \
    fontconfig \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

# Copiar entorno virtual generado en el builder
COPY --from=builder /app/.venv /app/.venv

COPY conf/ ./conf/
COPY controllers/ ./controllers/
COPY services/ ./services/
COPY app.py .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["./entrypoint.sh"]
