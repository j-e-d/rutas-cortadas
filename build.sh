#!/usr/bin/env bash
# Rebuild site/data.json from an estadorutas clone (default: ../estadorutas).
set -euo pipefail
cd "$(dirname "$0")"
repo="${1:-../estadorutas}"
mkdir -p build
python3 scripts/history.py "$repo" build
python3 scripts/viz_data.py build/rutas_changes.csv site/data.json
