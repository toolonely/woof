#!/bin/bash

# test wrapper that works with the test script

while true; do
    echo "(re)starting ./output.py"
    ./output.py | {
        while IFS= read -r line
        do
            echo "$line"
            if [[ "$line" =~ "disconnected" ]]; then
                kill $(pgrep -f output.py)
                echo "./output.py killed"
            fi
        done
    }
done
