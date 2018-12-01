#!/bin/sh
set -e
cp -a /app/template/* /output/
cd /app
python3 papyri.py --banners --mcdata /data/world --output /output
