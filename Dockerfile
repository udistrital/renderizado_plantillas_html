#
# 1. Build stage
#
FROM ghcr.io/astral-sh/uv:python3.12-alpine AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Paquetes de compilación para Alpine (cffi, WeasyPrint y librerías C)
RUN apk add --no-cache \
    build-base \
    python3-dev \
    libffi-dev \
    cairo-dev \
    pango-dev \
    gdk-pixbuf-dev

# Instalar dependencias del proyecto
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project --no-dev

#
# 2. Final stage
#
FROM python:3.12-alpine

WORKDIR /app

# Variables de entorno para Python y Flask
ENV PORT=8080 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# Librerías de ejecución para WeasyPrint, fuentes y utilidades
RUN apk add --no-cache \
    pango \
    cairo \
    harfbuzz \
    gdk-pixbuf \
    libffi \
    font-liberation \
    fontconfig \
    shared-mime-info \
    bash

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
