#!/bin/sh

set -e

printf "$(tput bold)$(date +%H:%M:%S)$(tput sgr0) Building... "

gilderoy

tput setaf 2
echo "done"
tput sgr0
