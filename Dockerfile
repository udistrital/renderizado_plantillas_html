ARG PYTHON_IMAGE=python:3.14-slim-trixie
ARG UV_VERSION=0.12.17

FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv

#
# 1. Build stage
#
FROM ${PYTHON_IMAGE} AS builder

# Copiar los binarios de uv directamente desde la imagen oficial
COPY --from=uv /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Instalar dependencias del proyecto
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project --no-dev

#
# 2. Final stage
#
FROM ${PYTHON_IMAGE}

WORKDIR /app

# Variables de entorno para Python y Flask
ENV PORT=8080 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# Dependencias de ejecución para WeasyPrint, fuentes y gráficos
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libharfbuzz0b \
    libharfbuzz-subset0 \
    libffi8 \
    ca-certificates \
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
