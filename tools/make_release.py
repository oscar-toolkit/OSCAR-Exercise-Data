# -*- coding: utf-8 -*-
"""Build the OSCAR example data release: OSCAR-Examples.zip, its .sha256 and manifest.json.

    python tools/make_release.py            (run from the examples folder)

The zip holds everything in this folder except README.md, tools/, dist/ and .git, with the folder layout of the
OSCAR data folder (Phantoms/..., Setups/...), so extracting it over Documents/OSCAR merges it. Attach the three
files in dist/ to a GitHub release of the OSCAR-Examples repository; OSCAR downloads
.../releases/latest/download/OSCAR-Examples.zip and checks it against the .sha256 file.
"""
import hashlib
import json
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_TOP = {"README.md", "tools", "dist", ".git", ".gitignore", ".gitattributes"}
SKIP_NAMES = {".gitkeep", "Thumbs.db", ".DS_Store"}
ASSET = "OSCAR-Examples.zip"


def files():
    for top in sorted(os.listdir(HERE)):
        if top in SKIP_TOP:
            continue
        base = os.path.join(HERE, top)
        if os.path.isfile(base):
            if top not in SKIP_NAMES:
                yield top, base
            continue
        for dp, dn, fn in os.walk(base):
            dn.sort()
            for f in sorted(fn):
                if f in SKIP_NAMES:
                    continue
                full = os.path.join(dp, f)
                yield os.path.relpath(full, HERE).replace(os.sep, "/"), full


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main():
    out = os.path.join(HERE, "dist")
    os.makedirs(out, exist_ok=True)
    zip_path = os.path.join(out, ASSET)
    listing = []
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for arc, full in files():
            zf.write(full, arc)
            listing.append({"path": arc, "bytes": os.path.getsize(full)})
            print("  +", arc)
    if not listing:
        sys.exit("Nothing to pack: put the example files in Phantoms/ and Setups/ first.")
    digest = sha256(zip_path)
    with open(zip_path + ".sha256", "w", encoding="ascii") as f:
        f.write(f"{digest}  {ASSET}\n")
    with open(os.path.join(out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump({"asset": ASSET, "sha256": digest, "files": listing}, f, indent=2)
    size = os.path.getsize(zip_path) / 1e6
    print(f"\n{ASSET}: {len(listing)} files, {size:.0f} MB, sha256 {digest[:16]}...")


if __name__ == "__main__":
    main()
