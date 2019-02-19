#!/usr/bin/env bash
ext=".blend"
newext=".off"
base= basename $1 $ext
mv "$1" "$(basename $1 $ext)$newext"
#cp $1 $newname
