#!/bin/bash
### Options
FILE=$1
DESTINATION="ToVideo"
DIGITCOUNT="%00d"
EXPORTFORMAT=".mp4"
QUALITY="-q:v 0" 
###

echo
echo "Found file $1"
FILENAME=${FILE%.*}
EXTENSION=${FILE#*.}
EXTENSION=.$EXTENSION
echo "Filename is: $FILENAME"
echo "Extension is: $EXTENSION"
FILENAME_NODIGITS=echo "$FILENAME" | sed 's/[0-9]//g'

shopt -s extglob
FILENAME_NODIGITS=${FILENAME%%+([[:digit:]])}
shopt -u extglob

echo "Filename no digits is: $FILENAME_NODIGITS"
echo

mkdir ../$DESTINATION
#mkdir ../$DESTINATION/$FILENAME_NODIGITS

echo "Converting "$1
echo " "
#ffmpeg -i $FILENAME_NODIGIT $QUALITY ../$DESTINATION/$FILENAME_NODIGIT/$FILENAME_NODIGIT$DIGITCOUNT$EXPORTFORMAT
ffmpeg -pattern_type glob -i "$FILENAME_NODIGITS*$EXTENSION" $QUALITY ../$DESTINATION/$FILENAME_NODIGITS$EXPORTFORMAT
echo " "
echo "Transcode Complete"
