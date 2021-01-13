#!/usr/bin/env python3

"""test wrapper that works with the test script"""

import subprocess

def main():
    """main"""
    while True:
        print("(re)starting ./output.py")
        proc = subprocess.Popen(["./output.py"], stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline().decode("utf-8").strip()
            print(line)
            if not line:
                break
            if "disconnected" in line:
                pid = subprocess.check_output(["pgrep", "-f", "output.py"]).decode("utf-8").strip()

                subprocess.Popen(["kill", pid])
                print("./output.py killed")


if __name__ == "__main__":
    main()
