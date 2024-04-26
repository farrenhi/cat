# Project Cat: 

## Implementation of a classic game in Command Line Interface to demonstrate the coding skills.

This project is my work to showcase the implementation of a classic game. It is built from the scratch. Several concepts are involved and designed in the codes as following. They will be discussed in details later in the Section B Code Design.

* Model-View-Controller (MVC) architecture design
* Object-Oriented Programming: instantiation of a class
* Multi-Threading process
* Unit Testing


## A. How to run this project
1. Clone this project to your local environment from my github page: https://github.com/farrenhi/cat/tree/main

2. If your computer is not installed with Python, you will need to install Python firstly. Related info in Python official website. https://www.python.org/

3. Install related libraries. The following are libraries (and version info) I used. You probably do not need to install exact version, but just as a reference.
* pytest 8.1.1
* requests 2.31.0
* requests-mock 1.12.1
By the way, my python version is Python 3.11.4. And, the project is not build with virtual environment.

4. In terminal, move to the local folder of this project. (The same level as controller.py)

5. Run the following command in terminal. Then, you should see that the game is starting! Enjoy it!

    ```bash
    python controller.py
    ```

    or

    ```bash
    python3 controller.py
    ```


## B. Code Design
### - Model-View-Controller (MVC) architecture design
![Alt Text](images/mvc.jpg)
Question: how to implement the codes in different platforms?

I have 3 phases of development work starting from the scratch. 

Phase 1 was simply to lay out several modules/functions to make the code run. However, I started to think about how to run the code on different platforms as mentioned in the guidance (web page, mobile app, command line etc). The question was that if I switched to web page design, then which part of codes should I work on? Furthermore, which part of codes were remained unchanged? Things became clear when I thought of the concept of Model-View-Controller (MVC) architecture design. This would be the onset of next phase 2.

Phase 2 was to convert my codes (modules/functions) into MVC design. In this design pattern, things would be easier to render the view layer on different platforms. The solution is to change view layer for different applications (web page/mobile app/etc). The controller layer and model layer remain unchanged or slightly changed. The view layer is to render the result or to take input from a user. The controller layer is to communicate between view layer and model layer. The game flow is in the controller layer. Finally, model layer processes data and validates the user input. Details in each layer would be discussed in next paragraph.

Let's walk through what is in each layer. 

Firstly, the core logic block is in model layer. The validate function is to verify the user input with secret code and to provide True/False results. The announce function would take the validation result and convert it into human readable feedback statement. The get_code function is to call external API for secret code for the game. 

Secondly, controller layer is served as a bridge between model layer and view layer. The play function is to control the game flow, and to execute functions from different layers. The get_valid_attempt function is to make sure a valid user input. The function would execute the function from model layer to check if valid. If not valid, the control layer function would execute functions in view layer to ask user to guess again.

Lastly, view layer is designed to interact with a user. The functions are used to ask for user input or to show user output/data. For example, the ask_user_guess function is to ask user to enter their guess of numbers. The present_to_user function is to render the results from control layer to user. The print_history function is to present history data of guesses and feedbacks to user.

Overall, the implementation of MVC design would make the transition of platforms more smoothly. Furthermore, our next question is that what if we have multi-players in a game? This type of question would bring us to the next phase. Phase 3 is instantiation of a class in object-oriented programming. Let me walk you through the concept in the next section.

### - Object-Oriented Programming: instantiation of a class
![Alt Text](images/class.jpg)
Question: how to implement multi-players?

What if we have several players in a game? This situation is similar to a classical software engineering topic: banking accounts. Each account is an instantiation of a class. To open a new bank account for a person is just like to create a new instance from a class. Based on this concept, here comes the phase 3.

Phase 3 is to change the codes further into class/instance code structure. I built a class of Player in model layer to store any info related to a player as illustrated above. The instance of the class has multiple attributes to store the data. The class also has some functions. For example, the update function is to update an instance (a player) data like name, score, and feedbacks. The calculate_score function is to calculate a player's score based on the attributes of an instance. I will talk about details of scoring system in the other section.

I also made controller layer and view layer into class objects. As for the model layer, I only made a class of player. The rest of functions in the model layer is not in a class. I think it should be ok like this, because the logic does not change based on different players. All players are under the same logic, which is in the model layer.

### - Multi-Threading process
![Alt Text](images/multi.jpg)
Question: how to set up a timer?

While a user is playing a game, we want to run a timer counting down the time simultaneously. I use multi-threading to run timer while the play function is still ongoing. This timer would be triggered in the middle of the function play. When the timer is done, it would also end the current game. Then, the loop will go to next player's round.

### - Unit Testing
Question: how to make sure inputs and outputs are functioning correctly?

I use unit testing to ensure that a function is working well. Pytest is the python version package about unit testing. I also use doctest in some function for a quick and simple unit test.

The following steps show you how to run unit test on this project.

1. Go to the directory of unit_test folder.

2. Enter these commands separately in the terminal:
    
    ```bash
    pytest controller_test.py
    ```

    ```bash
    pytest model_test4.py
    ```

    ```bash
    pytest call_api_code_test.py
    ```

3. You will see test result in the terminal.

## C. Extensions
### - Configurable Difficulty Level: adjustment of number of numbers, support to give hints
I set up 3 difficulty levels: easy, medium, and hard. User could choose a difficulty level before starting the game. The configuration is stored as class attribute in the class of player. There are four parameters among different levels.

* (parameter: easy/medium/hard)

* duplicate: False/True/True. Duplicate numbers are allowed or not. Easy level has no duplicate numbers.

* total_values: 4/8/10. Easy level has secret code ranging from 0 to 3 (4 numbers). Ex: [0, 3, 1, 2] Hard level would have numbers from 0 to 9 (9 numbers). This parameter is to implement the adjustment of number of numbers that are used.

* announce_level: 0/1/2. This is related to the feedback on the validation result. Medium level has the same feedback style as the assignment. Hard level just reveals "You win!" or "Incorrect". (yes... I know it is too hard!) Easy level has more hints such as position info and number info. This parameter implements the support to give hints.

* max_attempts: 15/10/6. It is about how many times a user could guess. Medium level is default with 10 times. Easy level is 15 times, while hard level is only 6 times.




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

8. how to stop a player's round if time is up? how to set up this timer?
