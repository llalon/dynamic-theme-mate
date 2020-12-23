#!/bin/bash
# Adapted from https://github.com/mariusknaust/spotlight

backgroundsPath=$1

if [ -z "$1" ]
  then
    backgroundsPath="$HOME/Pictures/spotlight"
fi


function decodeURL
{
	printf "%b\n" "$(sed 's/+/ /g; s/%\([0-9A-F][0-9A-F]\)/\\x\1/g')"
}

response=$(wget -qO- -U "WindowsShellClient/0" "https://arc.msn.com/v3/Delivery/Cache?pid=279978&fmt=json&lc=en,en-US&ctry=US")
item=$(jq -r ".batchrsp.items[0].item" <<< $response)
landscapeUrl=$(jq -r ".ad.image_fullscreen_001_landscape.u" <<< $item)
sha256=$(jq -r ".ad.image_fullscreen_001_landscape.sha256" <<< $item | base64 -d | hexdump -ve "1/1 \"%.2x\"")
title=$(jq -r ".ad.title_text.tx" <<< $item)
searchTerms=$(jq -r ".ad.title_destination_url.u" <<< $item | sed "s/.*q=\([^&]*\).*/\1/" | decodeURL)

mkdir -p "$backgroundsPath"
imagePath="$backgroundsPath/$(date +%y-%m-%d-%H-%M-%S)-$title ($searchTerms).jpg"

wget -qO "$imagePath" "$landscapeUrl"
sha256calculated=$(sha256sum "$imagePath" | cut -d " " -f 1)

if [ "$sha256" != "$sha256calculated" ]
then
	echo "Checksum incorrect"
	exit 1
fi