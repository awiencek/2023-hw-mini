"""
Use analog input with photocell
"""

import time
import machine
import os
import json

def get_params(param_file: str) -> dict:
    """Reads parameters from a JSON file."""

    if not is_regular_file(param_file):
        raise OSError(f"File {param_file} not found")

    with open(param_file) as f:
        params = json.load(f)

    return params


def is_regular_file(path: str) -> bool:
    """Checks if a regular file exists."""

    S_IFREG = 0x8000

    try:
        return os.stat(path)[0] & S_IFREG != 0
    except OSError:
        return False

led = machine.Pin("LED", machine.Pin.OUT)
adc = machine.ADC(28)

blink_period = 0.1

params = get_params("exercise04.json")
max_bright = params["max_bright"]
min_bright = params["min_bright"]

while True:
    value = adc.read_u16()
    print(value)
    duty_cycle = (value - min_bright) / (max_bright - min_bright)
    led.high()
    time.sleep(blink_period * duty_cycle)
    led.low()
    time.sleep(blink_period * (1 - duty_cycle))
