#!/bin/bash

for Event in /dev/input/event*; do
	if timeout 0.01 evtest $Event | grep -q BTN_STYLUS; then
		echo Pen Device Found
		echo $Event
		PenDevice=$Event
	fi
done

# Listen for BTN_TOOL_RUBBER events.

echo Remapping Button

evtest $PenDevice | while read line; do
for value in {0..1}; do
    echo $line|grep -q "type 1 (EV_KEY), code 321 (BTN_TOOL_RUBBER), value $value"
    if [[ $? == 0 ]]; then
        case $value in
            0)  xdotool mouseup 3   ;;
            1)  xdotool mousedown 3 ;;
        esac
    fi
done
done
