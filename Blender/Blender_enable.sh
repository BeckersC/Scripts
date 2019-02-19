#!/usr/bin/env bash
ext=".off"
newext=".blend"
base= basename $1 $ext
mv "$1" "$(basename $1 $ext)$newext"
#cp $1 $newname
