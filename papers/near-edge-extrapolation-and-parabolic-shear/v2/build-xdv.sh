#!/bin/sh
# Source compilation only: never creates a reader PDF.
set -eu
PAPER_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$PAPER_DIR"
mkdir -p tmp/build
: "${PAPER_TECTONIC:=tectonic}"
"$PAPER_TECTONIC" --outfmt xdv --keep-logs --keep-intermediates --outdir tmp/build main.tex
python3 checks/source_quality.py --build-dir tmp/build
