summary of work/miniproject
all information is also found in individual files in this repo

# Questions
these are also answered within the .md file of each exercise

## Exercise 1
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


## Exercise 2
### .json
{
    "loop_count": 100,
    "sleep_time": 0.01
}

### Question 01

Why do you think we would use a file (e.g. JSON file) for parameter storage instead of accepting the parameters as user `input()`, especially on an embedded system?

#### Answer 1
The user may not have the access to input when the program is implemented on a chip like raspberry pi pico. A json file is needed for the parameters. Additionally, it makes sure the parameters are set to usable values to prevent errors from user input.

### Question 02

Why might we prefer to use a JSON file to store parameters instead of hard-coding values in the Python script?

#### Answer 2
It is easier and more clear if we set the parameter in a separate file. This allows the parameters to be changes/updated later more easily if it becomes necessary to do so.

### Question 03

Why didn't the exercise02.py code use
[os.path.isfile](https://docs.python.org/3/library/os.path.html#os.path.isfile),
that is, why did I write the "is_regular_file()" function?

#### Answer 3
Micropython has fewer built in libraries/functions than python normally does. Without checking with the is_regular_file() function, you can get an error message from the file not being found (essentially, os.path.isfile does not work on its own in micropython).

## Exercise 3
### Question 1

Suppose I want to add additional code that requires me to increase sample time, to allow more time for the additional code to execute.
What is the tradeoff when I increase sample time relative to the "dot_dash_threshold" value?
Try this by increasing "sample_ms" in exercise3.json on the Pico.
The effect should be quite noticeable.

#### Answer 1
If the sample time is increased too much the program can no longer differentiate between a dot and a dash input. It should be less than the dot_dash_threshold value.

## Exercise 4
{
  "max_bright": 17000,
  "min_bright": 9000,
}

## Project 1
### Parameters (.json)
{
    "num_flash": 5,
    "sample_ms": 10.0,
    "on_ms": 500,
    "min_response_time": 0,
    "max_response_time": 0,
    "avg_response_time": 0,
    "score": ""
}

### Responses (.json)
{"min_response_time": 235, "sample_ms": 10.0, "avg_response_time": 287.3333, "num_flash": 5, "on_ms": 500, "score": "misses 2 / 5 times", "max_response_time": 369}

## Project 2
### Parameters (.json)
{
    "num_flash": 5,
    "sample_ms": 10.0,
    "on_ms": 500,
    "min_response_time": 0,
    "max_response_time": 0,
    "avg_response_time": 0,
    "score": ""
}
### Responses (.json)
{
    "num_flash": 3,
    "sample_ms": 10.0,
    "on_ms": 500,
    "min_response_time_1": 0,
    "max_response_time_1": 0,
    "avg_response_time_1": 0,
    "score_1": "",
    "min_response_time_2": 0,
    "max_response_time_2": 0,
    "avg_response_time_2": 0,
    "score_2": ""
}
