# Exercise 02 - deterministic code

[Exercise Python script](./exercise02.py)

[Exercise 02 Questions](#questions)

A common task in embedded systems is to repeat a task many times with a precise enough time interval.
Since we expect deterministic execution, there should be little variance in time to execute vs. what happens on a non-real-time system such as full Raspberry Pi with a non-real-time operating system or a laptop computer.
However, if the task is waiting on communication, IO or has random time delay, the execution time will vary.

Here we measure elapsed time, but add hardware in the loop.
This example runs only on the Pico as it uses the "machine" MicroPython module.

Note: to transfer files such as
[exercise02.json](./exercise02.json)
to the Pico, use Thonny IDE "View - Files".
Then in the "Files" top window for "This Computer", navigate to the file to copy to the Pico.
Right click that file, and select "Upload to /" to copy the file to the Pico.

In this exercise, copy both "exercise02.py" and "exercise02.json" to the Pico so that the Pico can load the parameter file without relying on the computer.
Edit / run the exercise02.py script on the Pico -- with Thonny this is done from the Files tab by right-clicking exercise02.py and selecting "open in Thonny".
Thonny shows tab "[exercise02.py]" where the brackets `[]` indicate the file is remote on the Pico.

For future reference (not necessary for this specific exercise): to download a file that you've edited on the Pico back to your computer to upload to Git, in Thonny Files tab, right-click the file on the Pico and select "Download to ..." where "..." is the directory on your computer to save the file.

## Questions

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
