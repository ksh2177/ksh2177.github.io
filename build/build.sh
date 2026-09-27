#!/usr/bin/env bash
# Régénère le site, les deux CV PDF et les deux CV Word depuis build/content.py.
# Dépendances : python3, chromium (les .docx sont écrits sans dépendance).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p assets
cp build/assets/logo-light.png build/assets/logo-dark.png assets/
python3 build/site.py
python3 build/cv.py fr
python3 build/cv.py en
python3 build/docx.py fr
python3 build/docx.py en
