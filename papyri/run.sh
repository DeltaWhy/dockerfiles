#!/bin/sh
set -e
cp -a /app/template/* /output/
python papyri.py --banners --mcdata /data/world --output /output
