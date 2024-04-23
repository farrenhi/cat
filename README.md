# project cat

Work log

I will start from the easiest implementation. It means that I would simplify the tasks firstly.
It could be oversimplified, but the first step is to make the code work firstly!


Module 1: Use the API to get the secret code
file: getcode.py
Done

Module 2: Validate the guess with the secret code
Done

Module 3: Show the validation result
Done

Module 4: history data
short term solution: just a matrix
long term solution: SQL database to record each attempt

Module 5: Main function to get every Module into this one for game play.
short term solution: command line
feature-history: this would keep track of each attempt and corresponding feedback.

long term solution: web page (docker image and to be deployed on AWS EC2 with RDS-MySQL)
(but long term solution might be hard within just a week window work time)



python doctest: 
python -m doctest -f -v module.py
    -m stands for "module" and is used to specify that you want to run a module as a script. In this case, it tells Python to run the doctest module and execute its functionality.

    -f stands for "fail fast" and is an optional flag used with doctest. When -f is specified, if a test fails, the testing process will stop immediately, and the error will be reported. Without -f, the testing process continues, and all test results are displayed at the end.

    -v stands for "verbose" and is another optional flag used with doctest. When -v is specified, it enables verbose mode, which provides more detailed output during testing, including information about each test that is being run and whether it passes or fails.



- potential issues and how I have solved it.
1. duplicate selection in getcode.py. Recursion issue. Solution: isolation of the function
(I thought duplicate is hard but actually, non duplicate is hard due to external API)
(one digit per request? or 4 digit per request?)
future task: one digit per request!

2. duplicate: my current design won't reflect the situation as indicated in assignment:
"0 1 3 5", and the guess is "2 2 1 1". number_boolean = [F, F, T, T]
but only 1 correct number...
So, I had to use counter separately to calculate the correct number by min(..., ...)

3. user input validation. need to make sure the user input is correct (4 digits and 4 number)

4. feature-timer setup
feature-timer-flashing: this branch would demo the flashing counting down, however, it is very hard to do flashing while user is inputting data... I think it is a dead-end. Could we check this out? Currently, this method is not used in my code

feature-timer: the implementation of countdown timer. however, global variable is used. I don't think it is a good practice. So, I might need to change it as dictionary item or something could be update by different functions. "Mutable Data Types". future task: change it to mutable data types

So, remaining_time is put into shared_vairables.py. This would be dynamically changed.

5. concurrency: when the timer is up, it would end the program. But, what if the user input attempts are done, it should also end the process! How to integrate this? (my solution: use a switch in function of count down timer)

6. unit test/doctest on function get_code. random number as output. cannot just default one...
Future task: try pytest

7. Change the code to Class/instantiation for multi player implementation.
