#!/usr/bin/env bash
# Régénère le site et les deux CV depuis build/content.py. Dépendances : python3, chromium.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p assets
cp build/assets/logo-light.png build/assets/logo-dark.png assets/
python3 build/site.py
python3 build/cv.py fr
python3 build/cv.py en
