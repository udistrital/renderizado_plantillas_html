#!/usr/bin/env bash

set -e
set -u
set -o pipefail

echo "Starting Renderizado Plantillas HTML Service..."

exec gunicorn \
    --bind 0.0.0.0:${RENDERIZADO_HTML_PORT:-8080} \
    --workers 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    app:app