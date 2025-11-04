#!/usr/bin/env python3
"""
Download two JWST files from MAST by product filename (program 4125).

For more info see:
https://jwst-docs.stsci.edu/accessing-jwst-data/mast-api-access#gsc.tab=0
"""
from astroquery.mast import Observations
from pathlib import Path

# Specify the filenames to download, as well as the directory to download them into
data = {
    "NIRSpec": {
        "data_dir": "Cosmic_Eye/NIRSpec/reduced/stage1/",
        "filenames": [f"jw04125018001_02101_0000{i}_nrs1_rate.fits" for i in (1, 2)],
    },
    "NIRCam": {
        "data_dir": "Cosmic_Eye/NIRCam/reduced/stage1/",
        "filenames": [
            f"jw04125017001_02103_0000{i}_nrc{x}long_rate.fits" for i in (1, 2) for x in "ab"
        ],
    },
}
# loop through the two instruments and download all the listed files
for instrument in data.keys():
    # set up the directory that the files will be downloaded into
    outdir = Path(data[instrument]["data_dir"])
    # check if the directory exists, if not make it
    outdir.mkdir(parents=True, exist_ok=True)

    for filename in data[instrument]["filenames"]:
        # MAST uses "Uniform Resource Identifiers" (uri) to uniquely identify files
        uri = f"mast:JWST/product/{filename}"
        # Save into the specified directory; keep original filenames
        local_path = Observations.download_file(uri, local_path=str(outdir), cache=False)
        print(f"Downloaded: {filename} {local_path}")
