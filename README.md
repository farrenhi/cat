# cat

Work log

I will start from the easiest implementation. It means that I would simplify the tasks firstly.
It could be oversimplified, but the first step is to make the code work firstly!


Module 1: Use the API to get the secret code
file: getcode.py

Module 2: Validate the guess with the secret code

Module 3: Show the validation result

Module 4: history data
short term solution: just a matrix
long term solution: SQL database to record each attempt


Module 5: Main function to get every Module into this one for game play.
short term solution: command line
long term solution: web page (docker image and to be deployed on AWS EC2 with RDS-MySQL)
(but long term solution might be hard within just a week window work time)



- potential issues and how I have solved it.
1. duplicate selection in getcode.py. Recursion issue. Solution: isolation of the function