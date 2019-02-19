#!/usr/bin/env bash

for f in *.blend; do
    blender $f -b -a
done
