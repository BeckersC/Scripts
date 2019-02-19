#!/bin/bash
### Options
FILE=$1
DESTINATION="Image_Sequence"
DIGITCOUNT="%07d"
EXPORTFORMAT=".jpg"
QUALITY="-q:v 0" 
###

echo
echo "Found file $1"
FILENAME=${FILE%.*}
EXTENSION=${FILE#*.}
EXTENSION=.$EXTENSION
echo "Filename is: $FILENAME"
echo "Extension is: $EXTENSION"
echo

mkdir ../$DESTINATION
mkdir ../$DESTINATION/$FILENAME

echo "Converting "$1
echo " "
ffmpeg -i $FILE $QUALITY ../$DESTINATION/$FILENAME/$FILENAME$DIGITCOUNT$EXPORTFORMAT
echo " "
echo "Transcode Complete"
