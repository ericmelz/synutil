#!/bin/bash
#set -ex

# Main code to rsync from source to dest
SOURCE=$1
DEST=$2
echo "Rsyncing from '$SOURCE' to '$DEST'"

start=$(date +%s)
rsync -avh --delete --progress "$SOURCE" "$DEST"
end=$(date +%s)
elapsed=$((end-start))
mb=$(du -sm "$SOURCE" | awk '{print $1}')
mb_s=$(echo "scale=2; $mb/$elapsed" | bc)
echo "Elapsed: $elapsed seconds"
echo "MB: $mb"
echo "Transfer speed: $mb_s MB/s"
