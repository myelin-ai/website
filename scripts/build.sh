#!/bin/sh

set -e

version_file() {
    FILE="$1"
    PREFIX="public"
    EXTENSION="${FILE##*.}"
    FILENAME="${FILE%.*}"
    VERSIONED="$FILENAME-$(shasum "$PREFIX/$FILE" | awk '{print $1}' | cut -c1-10).$EXTENSION"

    mv "$PREFIX/$FILE" "$PREFIX/$VERSIONED"

    echo $VERSIONED
}

tput setaf 6
echo "[$(date +%H:%M:%S)] Building..."
tput sgr0

mkdir -p public/static
sass sass/style.scss --style compressed > public/static/style.css

./scripts/render.py --css-file=$(version_file static/style.css)
