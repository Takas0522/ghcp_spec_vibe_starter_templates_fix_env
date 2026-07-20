#!/usr/bin/env bash
set -euo pipefail

python -m pip install --upgrade pip

# Install repository-managed dependencies when present.
if [[ -f requirements.txt ]]; then
  python -m pip install -r requirements.txt
fi

if [[ -f requirements-dev.txt ]]; then
  python -m pip install -r requirements-dev.txt
fi

# Baseline packages aligned with the repository's intended Python web stack.
python -m pip install \
  fastapi \
  "uvicorn[standard]" \
  pytest \
  httpx \
  "passlib[bcrypt]" \
  PyJWT
