#
# 1. Build stage
#
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Add libffi-dev to the cffi compilation (dependency WeasyPrint)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv sync --frozen --no-install-project --no-dev

#
# 2. Final stage
#
FROM python:3.12-slim-bookworm

WORKDIR /app

# Variables de entorno para Python y Flask
ENV PORT=8080 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# Dependency WeasyPrint
# Add libgdk-pixbuf2.0-0 to images support
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi8 \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# Copy venv from the builder
COPY --from=builder /app/.venv /app/.venv

COPY conf/ ./conf/
COPY controllers/ ./controllers/
COPY services/ ./services/
COPY app.py .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh &&

EXPOSE 8080

ENTRYPOINT ["./entrypoint.sh"]