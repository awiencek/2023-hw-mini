# Exercise 03 - Capture time-pattern of button presses - Morse Code

[Exercise Python script](./exercise03.py)

[Exercise 03 Questions](#questions)

[Morse code table from wikipedia.org/wiki/File:International_Morse_Code.svg (public domain)](./morse_code.png)

This Python script is a rudimentary
[Morse Code](https://en.wikipedia.org/wiki/Morse_code)
decoder and playback system using a tactile switch and onboard LED.
The tactile switch is used to enter Morse Code, and the onboard LED is used to playback the Morse Code.

The tactile switch is connected between GPIO 16 and ground.
Or, you can change this line of code if you wish to use another GPIO pin.
This is indicated by the line of code

```python
button = Pin(16, Pin.IN, Pin.PULL_UP)
```

because we've chosen the pin to be "PULL_UP" this means internal to the RP2040 CPU, there is a resistor connected inline with 3V3 supplied to GPIO 16.
Connecting GPIO 16 with pull up to ground via the tactile switch is sensed by the CPU as a near-zero voltage i.e. "active low" which is used in Python code line

```python
if button.value() == 0:
```

Numerous microcontroller implementations of Morse Code decoders have existed for decades.
This one is very simple, but is enough to demonstrate time-dependent reading of a digital input.

A more correct implementation would use dot-dash ratios instead of fixed dot/dash times.
We're not going to do that here, but it leads into Question 1.
That is, in a real system, we'd want to be running more code than this that requires us to not have such a "good" i.e. small sample time.
That's because each loop iteration must complete within the allotted time (especially if in the same thread, but even if in a separate thread) to measure dot-dash timing.

## Questions

### Question 1

Suppose I want to add additional code that requires me to increase sample time, to allow more time for the additional code to execute.
What is the tradeoff when I increase sample time relative to the "dot_dash_threshold" value?
Try this by increasing "sample_ms" in exercise3.json on the Pico.
The effect should be quite noticeable.

#### Answer 1
If the sample time is increased too much the program can no longer differentiate between a dot and a dash input. It should be less than the dot_dash_threshold value.
