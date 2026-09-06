#!/bin/sh
# Build the independent submission copy with standard pdfLaTeX and BibTeX.
set -eu
PAPER_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PAPER_BUILD_DIR=${PAPER_BUILD_DIR:-"$PAPER_DIR/tmp/build"}
PAPER_PDFLATEX=${PAPER_PDFLATEX:-pdflatex}
PAPER_BIBTEX=${PAPER_BIBTEX:-bibtex}
mkdir -p "$PAPER_BUILD_DIR"
cd "$PAPER_DIR/source"
"$PAPER_PDFLATEX" -no-shell-escape -interaction=nonstopmode -halt-on-error -recorder -output-directory="$PAPER_BUILD_DIR" main.tex > "$PAPER_BUILD_DIR/pass-1.log" 2>&1
cp references.bib "$PAPER_BUILD_DIR/references.bib"
(
  cd "$PAPER_BUILD_DIR"
  "$PAPER_BIBTEX" main > bibtex-console.log 2>&1
)
cp "$PAPER_BUILD_DIR/main.bbl" main.bbl
"$PAPER_PDFLATEX" -no-shell-escape -interaction=nonstopmode -halt-on-error -recorder -output-directory="$PAPER_BUILD_DIR" main.tex > "$PAPER_BUILD_DIR/pass-2.log" 2>&1
"$PAPER_PDFLATEX" -no-shell-escape -interaction=nonstopmode -halt-on-error -recorder -output-directory="$PAPER_BUILD_DIR" main.tex > "$PAPER_BUILD_DIR/pass-3.log" 2>&1
printf 'PDF build complete: %s/main.pdf\n' "$PAPER_BUILD_DIR"
