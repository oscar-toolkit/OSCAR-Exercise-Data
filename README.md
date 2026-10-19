# OSCAR Examples

Example data for [OSCAR](https://github.com/oscar-toolkit/OSCAR): phantoms, a CT scan, texture blends and
setups to work through while learning the toolkit.

## Getting the data

In OSCAR choose **Help > Download Example Data…**. The files are added to your OSCAR data folder
(`Documents\OSCAR` by default); anything you already have there is kept.

To do it by hand, download `OSCAR-Examples.zip` from the
[latest release](https://github.com/oscar-toolkit/OSCAR-Examples/releases/latest) and extract it over your OSCAR
data folder. The zip has the same folder layout, so it merges.

## What is in it

```
Phantoms/
  NCAT Phantoms/          NCAT phantoms (.nrb) for the NURBS tab
  CT Reference Data/      an example CT scan for CT -> Voxelized
  Texture Recipes/Blends/ blends used by the examples (.texblend)
Setups/                   example setups (.oscarsetup)
```

## For maintainers

This folder is its own repository. The data is not committed: it is attached to a release, so the repository stays
small and a clone is quick.

1. Put the files in `Phantoms/` and `Setups/` as above.
2. Run `python tools/make_release.py`. It writes `dist/OSCAR-Examples.zip`, `dist/OSCAR-Examples.zip.sha256` and
   `dist/manifest.json`.
3. Create a release and attach the three files. OSCAR downloads
   `releases/latest/download/OSCAR-Examples.zip` and checks it against the `.sha256` file.

A mirror (for example a Zenodo record) can be used by setting `examples_url` in `~/.oscar_settings.json`.
