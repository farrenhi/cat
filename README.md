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
