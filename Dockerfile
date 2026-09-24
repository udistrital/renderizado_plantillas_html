#
# 1. Build stage
#
FROM ghcr.io/astral-sh/uv:0.5-ubuntu24.04 AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Instalar Python 3.14 y librerías de compilación usando uv
RUN uv python install 3.14

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./

RUN uv sync --python 3.14 --frozen --no-install-project --no-dev

#
# 2. Final stage
#
FROM ubuntu:24.04

WORKDIR /app

ENV PORT=8080 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libffi8 \
    fonts-liberation \
    fontconfig \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/.venv /app/.venv

COPY conf/ ./conf/
COPY controllers/ ./controllers/
COPY services/ ./services/
COPY app.py .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["./entrypoint.sh"]
