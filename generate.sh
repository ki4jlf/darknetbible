#!/bin/bash

set -ex

# Generate public directory
rm -rf public
hugo --theme book

# Generate offline directory
rm -rf offline
mkdir -p offline/content
cp -a public/* offline/content
cp public/index.html offline/
python3 process_offline.py

# Get date of last commit
DATE=$(git log -1 --format="%at" | xargs -I{} date -d @{} +%Y-%m-%d)
VER=bible-$DATE
echo "$DATE" > date.txt

# Zip the offline directory
rm -rf $VER $VER.zip
mv offline $VER
zip -r $VER.zip $VER

# Copy offline zip to public directory
mkdir -p public/static
cp $VER.zip public/static

# Process public
python3 process_public.py
