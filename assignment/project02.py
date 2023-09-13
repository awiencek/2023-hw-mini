"""
Response time & Light intensity - dual-threaded
(using project01.py as a base)
"""

from machine import Pin
import time
import random
import os
import json
import _thread

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

led = Pin("LED", Pin.OUT)
button01 = Pin(16, Pin.IN, Pin.PULL_UP)
button02 = Pin(26, Pin.IN, Pin.PULL_UP)

params = get_params("project01.json")
N: int = params["num_flash"]
sample_ms = params["sample_ms"]
on_ms = params["on_ms"]

def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(N: int) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


t1: list[float | None] = []
t2: list[float | None] = []

blinker(3)

for i in range(N):
    time.sleep(random_time_interval(0.5, 5.0))

    led.high()

    tic = time.ticks_ms()
    t01 = None
    t02 = None
    while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
        if button01.value() == 0:
            t01 = time.ticks_diff(time.ticks_ms(), tic)
            led.low()
            break
        elif button02.value() == 0:
            t02 = time.ticks_diff(time.ticks_ms(), tic)
            led.low()
            break
        elif button01.value() == 0 and button02.value() ==0:
            t01 =time.ticks_diff(time.ticks_ms(), tic)
            t02 = t01
            break
    t.append(t01)
    t.append(t02)

    led.low()

blinker(5)

# %% collate results
misses = t.count(None)
print(f"You missed the light {misses} / {N} times")

t_good = [x for x in t if x is not None]

# how to print the average, min, max response time + score?

print(t_good)
