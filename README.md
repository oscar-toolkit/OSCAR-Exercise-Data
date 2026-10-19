# OSCAR Example Data

Example data for [OSCAR](https://github.com/oscar-toolkit/OSCAR): phantoms, a CT scan, texture blends and
setups to work through while learning the toolkit.

## Getting the data

In OSCAR choose **Help > Download Example Data…**. The files are added to your OSCAR data folder
(`Documents\OSCAR` by default); anything you already have there is kept.

To do it by hand, download `OSCAR-Example-Data.zip` from the
[latest release](https://github.com/oscar-toolkit/OSCAR-Example-Data/releases/latest) and extract it over your OSCAR
data folder. The zip has the same folder layout, so it merges.

## What is in it

```
Sim Output/                      example simulation results
Setups/                          example setups (.oscarsetup)
Materials/                       example materials
Phantoms/
  Generated Phantoms/            example generated phantoms
  Configurations/                example phantom configurations
  NCAT Phantoms/                 five NCAT phantoms (.nrb) for the NURBS tab
  CT Reference Data/CCR Texture/ two CCR CT scans (CCR1_GE2, CCR1_GE6) for CT -> Voxelized
  Texture Recipes/
    Blends/                      six single-method blends at the Blend Creator's defaults:
                                 Perlin, Fractal, Voronoi, Gabor, Gaussian and Wave (4 waves)
    Fourier Spectra/             example Fourier spectra
  Custom Phantom Designs/        example analytic phantom designs
```

## For maintainers

This folder is its own repository. The data is not committed: it is attached to a release, so the repository stays
small and a clone is quick.

1. Put the files in `Phantoms/` and `Setups/` as above.
2. Run `python tools/make_release.py`. It writes `dist/OSCAR-Example-Data.zip`, `dist/OSCAR-Example-Data.zip.sha256` and
   `dist/manifest.json`.
3. Create a release and attach the three files. OSCAR downloads
   `releases/latest/download/OSCAR-Example-Data.zip` and checks it against the `.sha256` file.

A mirror (for example a Zenodo record) can be used by setting `examples_url` in `~/.oscar_settings.json`.
