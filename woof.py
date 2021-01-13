#!/usr/bin/env python3

"""
    wrapper for gnirehtet
    has to be in the same directory with gnirehtet, since it is called as ./
    - runs gnirehtet in a loop
    - when a client disconnects, gnirehtet prints a log message, but keeps
      working. the only way to fix it is to manually restart gnirehtet on the
      desktop
    - the wrapper detects the disconnect log message of gnirehtet and kills it,
      so the loop restarts gnirehtet again
    - after gnirehtet restarts, the phone connects again automatically, and
      the reverse tethering is restored
"""

import subprocess
import time

def main():
    """main"""
    while True:
        print("(re)starting ./gnirehtet")
        proc = subprocess.Popen(["./gnirehtet", "autorun"], stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline().decode("utf-8").strip()
            print(line)
            if not line:
                break
            if "disconnected" in line:
                pid = subprocess.check_output(["pgrep", "-f", "gnirehtet"]).decode("utf-8").strip()

                subprocess.Popen(["kill", pid])
                print("./gnirehtet.py killed")
                time.sleep(1)


if __name__ == "__main__":
    main()