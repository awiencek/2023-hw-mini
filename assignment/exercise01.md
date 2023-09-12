# Exercise 01 - Python fundamentals

[Python code](./exercise01.py)

[Exercise 01 Questions](#questions)

---

If you haven't already, please setup
[MicroPython on the Pico](../doc/micropython.md)
and the
[Thonny IDE](../doc/thonny.md).

---

Similar to
[C++ modules](https://en.cppreference.com/w/cpp/language/modules),
[Python modules](https://docs.python.org/3/tutorial/modules.html)
provide definitions such as objects,
[functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions),
and variables within a namespace.
We generally avoid mixing namespaces so we don't do "from module import *" as this can lead to name collisions and be confusing as to where a function comes from.

## Functions

A general good coding practice is to use functions (or object with methods) to encapsulate functionality.
This avoid mistyping and duplicating values or making unexpected side effects on variables or object properties in other parts of the program.
Breaking up code into functions and methods also facilitates unit testing to ensure parts of the code do what is expected.
I have seen teams waste a month or more because they had a monolithic main program and did not test individual pieces, and there was a simple mistake messing up their whole project that would have been trivially caught by unit testing.

## Print formatting

Note that we use
[f-string notation](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings)
to print with formatting.
In general it is import to format print of floating point number significant precision.
This avoids a common mistake of printing all the available digits, which often have little meaning and imply precision that does not exist.
Does the system really have precision of say elapsed time in femtoseconds or voltage in picovolts?

## measuring elapsed time

The MicroPython
[time](https://docs.micropython.org/en/latest/library/time.html)
module has some missing and additional functions vs. the CPython
[time](https://docs.python.org/3/library/time.html)
module.
Older versions of MicroPython used "utime" but this has been replaced by "time".
Many operations on microcontrollers concern time such as time delays or doing something on a strict periodic schedule, which is what utime can be used for.
Doing a periodic task with the highest precision can be done by specifying CPU ticks.
For tasks like flashing LEDs or sampling slowly updating sensors like photocells, CPU tick level precision is typically not needed.

For the variable "tic", in CPython on might be accustomed to using
[time.monotonic()](https://docs.python.org/3/library/time.html#time.monotonic)
but in current versions of MicroPython this function is not available.

## Questions

Note: when running the code in MicroPython with Thonny, when typing the input response, click the mouse in the line below where Python requests input and then type response and press Enter.

### Question 01

Before running the exercise01.py program, about how long do you think the program above will take to run?
Did you have the right answer -- what does the program print out?

#### Answer 1
before running:
10 loops, 1second
we predict it will take 10 seconds to run

actual output (sleep_time): 10.012 seconds


### Question 02

What do the "int" and "float" notation mean?

Will the program run if these notations are removed or incorrect?

[Reference](https://docs.python.org/3/library/typing.html)

#### Answer 2
Numbers with the int type can only be integer values. Float allows the program to use decimal values as well.

The program would not run if these notations were removed/incorrect because any non integer values would cause an error.


### Question 03

Why is "time.ticks_diff(toc, tic)" used to determine elapsed time instead of "toc - tic"?

#### Answer 3
time.ticks_diff(toc, tic) will not incorrectly calculate the elapsed time if zero wraps around
