#!/usr/bin/env sh
set -eu

python3 -B -m unittest discover -s tests -v

