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

import os
import subprocess
import sys
import time

if os.name == "nt":
    pass
else:
    with open(os.devnull, "w") as devnull:
        child = subprocess.Popen(["which", "gnirehtet"], stdout=devnull, stderr=devnull)
        child.communicate()
        ret = child.returncode
        if ret != 0:
            os.environ["PATH"] = "{}:.".format(os.environ["PATH"])
        child = subprocess.Popen(["which", "gnirehtet"], stdout=devnull, stderr=devnull)
        child.communicate()
        ret = child.returncode
        if ret != 0:
            print("gnirehtet not found")
            print("either install it through a package for your OS")
            print("or download the Rust binary release from GitHub")
            sys.exit(-1)

def main():
    """main"""
    while True:
        print("(re)starting gnirehtet")
        try:
            proc = subprocess.Popen(["gnirehtet", "autorun"], stdout=subprocess.PIPE)
        except FileNotFoundError:
            print("gnirehtet not found")
            sys.exit(-1)
        while True:
            line = proc.stdout.readline().decode("utf-8").strip()
            print(line)
            if not line:
                break
            if "disconnected" in line:
                if os.name == "nt":
                    subprocess.Popen(["taskkill", "/f", "/im", "gnirehtet.exe", "/t"])
                else:
                    pid = subprocess.check_output(["pgrep", "-f", "gnirehtet"]).decode("utf-8").strip()

                    subprocess.Popen(["kill", pid])
                print("gnirehtet killed")
                time.sleep(1)


if __name__ == "__main__":
    main()
