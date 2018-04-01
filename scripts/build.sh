#!/bin/sh

set -e

printf "$(tput bold)$(date +%H:%M:%S)$(tput sgr0) Building... "

mkdir -p public/static

sass sass/style.scss --style compressed > assets/style.css

./scripts/build.py

tput setaf 2
echo "done"
tput sgr0
