#!/bin/bash

# wrapper for gnirehtet
# - runs gnirehtet in a loop
# - when a client disconnects, gnirehtet prints a log message, but keeps
#   working. the only way to fix it is to manually restart gnirehtet on the
#   desktop
# - the wrapper detects the disconnect log message of gnirehtet and kills it,
#   so the loop restarts gnirehtet again
# - after gnirehtet restarts, the phone connects again automatically, and
#   the reverse tethering is restored

while true; do
    echo "(re)starting ./gnirehtet"
    ./gnirehtet autorun | {
        while IFS= read -r line
        do
            echo "$line"
            if [[ "$line" =~ "disconnected" ]]; then
                kill $(pgrep -f gnirehtet)
                echo "./gnirehtet killed"
                sleep 1
            fi
        done
    }
done
