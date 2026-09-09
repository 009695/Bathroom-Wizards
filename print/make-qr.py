#!/usr/bin/env python3
"""Generate QR codes for the business cards.

Re-run this whenever the live URLs change:
    python3 make-qr.py https://your-real-domain.co.uk
"""
import sys, pathlib
import segno

BASE = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "https://009695.github.io/kent-trades-web"

TARGETS = {
    "qr-handyfix":    f"{BASE}/handyfix/",
    "qr-bathrooms":   f"{BASE}/bathrooms/",
    "qr-shipwrights": f"{BASE}/shipwrights/",
}

out = pathlib.Path(__file__).parent / "qr"
out.mkdir(exist_ok=True)

for name, url in TARGETS.items():
    # error='h' survives a logo overlay and a scuffed card in a work van
    qr = segno.make(url, error="h")
    qr.save(out / f"{name}.svg", scale=10, border=2, dark="#000000")
    print(f"{name}.svg  ->  {url}   (version {qr.version})")

print(f"\nBase URL: {BASE}")
print("Re-run with a different base URL to repoint every card at once.")
