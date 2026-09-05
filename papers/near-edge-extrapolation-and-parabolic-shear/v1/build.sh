#!/bin/sh
# Local TeX build. No upload, deployment, or submission action.
set -e
PAPER_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$PAPER_DIR"
mkdir -p tmp/build output/pdf
if [ -z "$PAPER_TECTONIC" ]; then PAPER_TECTONIC=tectonic; fi
"$PAPER_TECTONIC" --keep-logs --keep-intermediates --outdir tmp/build main.tex
cp tmp/build/main.pdf output/pdf/near-edge-parabolic-shear.pdf
cp tmp/build/main.bbl main.bbl
