#!/bin/bash
#
# Regenerates the cv_*.tex fragments from _data/*.yml, then builds the five
# PDFs.
#
# JT normally typesets these in TeXShop using "TeX and DVI", which is
# latex -> dvips -> Ghostscript, NOT pdflatex. This script used to call
# pdflatex, which produces a valid but visibly different file: same text,
# ~19% larger, and a different /Producer. Following the script instead of the
# GUI silently changed the toolchain for all five PDFs on 29 July 2026.
#
# So the chain below deliberately mirrors TeXShop. Checked against a PDF JT
# typeset himself: identical rendered text, same dvips(k) 2026.1 creator, same
# Ghostscript producer, and a 54-byte size difference that is entirely the
# embedded CreationDate and the random PDF /ID. Two PDFs from this chain will
# never be byte-identical for that reason -- compare `pdftotext` output, not
# checksums.
#
# dvips is piped straight into ps2pdf so no .ps intermediates are left in the
# working tree; *.ps is not gitignored.

set -e

python3 parse_yaml.py

for doc in jthaler_cv \
           jthaler_cv_no_publications \
           jthaler_cv_just_publications \
           jthaler_cv_just_publications_last10 \
           jthaler_cv_top5_publications
do
  echo "building $doc"
  # Twice: the second pass settles page references. The CV currently needs only
  # one -- the second reports no "Rerun to get cross-references right" -- but a
  # single pass silently produces stale numbers the moment anything does.
  latex -interaction=nonstopmode "$doc.tex" > /dev/null
  latex -interaction=nonstopmode "$doc.tex" > /dev/null
  dvips -q -f "$doc.dvi" | ps2pdf - "$doc.pdf"
done

echo "done: 5 PDFs"
