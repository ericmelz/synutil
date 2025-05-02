#!/bin/bash

cd /Volumes/EricRandiShare/iTunes_Library/Music

find . -mindepth 2 -maxdepth 2 -type d ! -name '@eaDir' \
  -exec stat -f '%m %N' {} + \
| sort -nr \
| head -n 10 \
| cut -d' ' -f2-
