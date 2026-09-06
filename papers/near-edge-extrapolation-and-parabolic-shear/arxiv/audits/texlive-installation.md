# Local TeX Live 2025 verification runtime

Installed on 2026-09-06 into `/private/tmp/heat-edge-arxiv-texlive2025/2025`.

- Official TUG historic mirror: https://ftp.tu-chemnitz.de/pub/tug/historic/systems/texlive/2025/tlnet-final
- Mirror is listed at https://tug.org/historic/.
- Installer: install-tl-20260301, final TeX Live 2025 repository.
- This is the final repository snapshot, **not** arXiv's 2025-08-03 snapshot and not a remote arXiv compiler run.
- Scheme: basic; added booktabs, enumitem, mathtools, microtype, xcolor. Geometry, lm, natbib and other core manuscript packages were already present.
- Architecture: universal-darwin (ARM/x86_64).
- Runtime: pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025), BibTeX 0.99d (TeX Live 2025), kpathsea 6.4.1.
- tlmgr revision: 76773 (2025-11-06).
- All 16 directly required standard class/package/style files resolved via this runtime's kpsewhich.
- Portable installation: no sudo, no shell/system PATH changes, no desktop integration; configuration and runtime caches remain inside this temporary installation.
- Installer SHA512 matches the same HTTPS mirror's published checksum: `a307d7d11bcbd1f054ad0b0d476f7f12bc1a40d07445020edef8713b44453831d18a2f1722c3d2b0ea2e4fe6c06183a79d1c4049495113f412a9f5a570a8614d`.
- GPG executable was unavailable; detached OpenPGP repository signature verification was not performed. HTTPS certificate verification was retained.

## Binaries

`/private/tmp/heat-edge-arxiv-texlive2025/2025/bin/universal-darwin/pdflatex`

`/private/tmp/heat-edge-arxiv-texlive2025/2025/bin/universal-darwin/bibtex`

## Logs

`logs/install-tl.log`, `logs/install-console.log`, `logs/install-paper-packages.log`.

The exact installation profile and installer checksum are retained in `installer/`.
