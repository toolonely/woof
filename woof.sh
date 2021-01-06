#!/bin/bash

while true; do
    echo "(re)starting ./gnirehtet"
    ./gnirehtet autorun | {
        while IFS= read -r line
        do
            echo "$line"
            if [[ "$line" =~ "disconnected" ]]; then
                kill $(pgrep -f gnirehtet)
                echo "./gnirehtet killed"
            fi
        done
    }
done
