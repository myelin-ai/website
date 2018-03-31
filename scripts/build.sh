#!/bin/sh

set -e

tput setaf 6
echo "[$(date +%H:%M:%S)] Building..."
tput sgr0

sass sass/style.scss --style compressed > public/style.css
./scripts/render.py
