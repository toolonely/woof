#!/usr/bin/env python3

import time
import random

REGULAR_MESSAGE = "regular message"
ERROR_MESSAGE = "INFO TunnelServer: Client #0 disconnected"

error_printed = False

while True:
    time.sleep(1)
    if error_printed is True:
        continue
    random_number = random.randrange(10)
    if random_number < 9:
        print(int(time.time()), f"rand = {random_number}", REGULAR_MESSAGE)
    else:
        print(int(time.time()), f"rand = {random_number}", ERROR_MESSAGE)
        error_printed = True

