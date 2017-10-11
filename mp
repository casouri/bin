#!/bin/bash

# Use a dir as argument
# Create ~/Desktop/pkg.zip
# with content of the argument dir

cd "${1}"
cd ../
NAME="${1##*/}"
zip -r ~/Desktop/pkg.zip "$NAME"
