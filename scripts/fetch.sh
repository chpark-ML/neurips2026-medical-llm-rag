#!/usr/bin/env bash
# Download the official NeurIPS poster lists (title, authors, abstract) from neurips.cc/Downloads.
# Usage: bash scripts/fetch.sh   -> data/raw/neurips{2025,2026}_posters.json
set -euo pipefail
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
mkdir -p data/raw
for Y in 2025 2026; do
  CJ=$(mktemp)
  curl -s -A "$UA" -c "$CJ" -b "$CJ" "https://neurips.cc/Downloads/$Y" -o "$CJ.html"
  TOK=$(grep -o 'csrfmiddlewaretoken" value="[^"]*' "$CJ.html" | sed 's/.*value="//')
  curl -s -A "$UA" -c "$CJ" -b "$CJ" -e "https://neurips.cc/Downloads/$Y" -X POST "https://neurips.cc/Downloads/$Y" \
    --data "csrfmiddlewaretoken=$TOK&format=5&posters=on&resource=0&submitaction=Download+Data" \
    -o "data/raw/neurips${Y}_posters.json"
  rm -f "$CJ" "$CJ.html"
done
# Oral/spotlight decisions and track. Each download is a different partial subset, so keep
# dated snapshots; scripts/decisions.py merges every data/raw/neurips2026_orals_posters*.json.
curl -s -A "$UA" -o "data/raw/neurips2026_orals_posters_$(date +%F).json" https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json
python3 -c "import json;[print(f, len(json.load(open('data/raw/'+f)))) for f in ['neurips2025_posters.json','neurips2026_posters.json']]"
