import getcode
import validate
import show_result

print("Hello, are you ready for the game?")


### game configuration
difficulty_level = 1
duplicate = True
total_values = 8 # total is 8, but it would be between 0 and 7.
max_attempts = 10
###


#####################
num_attempts = 1

secret_code = getcode.get_code(total_values, duplicate)

# Future task: this would take a wile to generate non duplicate secret code
# how to solve this long wait?
print("Secret code is generated!", secret_code)

# Initialize an empty list to store user inputs
user_attempts = []
feedbacks = []

def validate_input(user_input):
    if len(user_input) != 4:
        return False
    if not user_input.isdigit():
        return False
    return True

def print_history(user_attempts, feedbacks):
    for attempt, feedback in zip(user_attempts, feedbacks):
        print(f"User Attempt: {attempt}, Feedback: {feedback}")

# while loop for 10 attempts
while num_attempts < max_attempts + 1:
    is_user_input_valid = False

    while is_user_input_valid is False:
        user_input = input("Guess a sequence of four numbers (example: 3102): ")
        # user_input is a string data type!
        if validate_input(user_input):
            is_user_input_valid = True
        else:
            print("Please input 4 digit of numbers.")

    user_attempt = [int(digit) for digit in user_input] # convert string into integer
    print(f"Your Guess Attempt {num_attempts}:", user_attempt)
    num_attempts += 1

    user_attempts.append(user_attempt)
    
    number_boolean, position_boolean, counter_correct_number = \
        validate.validate(secret_code=secret_code, user_attempt=user_attempt)

    feedback = show_result.announce(user_attempt, number_boolean, position_boolean, \
        counter_correct_number, difficulty_level)

    feedbacks.append(feedback)
    
    print(f"Number of guesses remaining:", max_attempts - num_attempts + 1)
    print('--------------------------')
    # print('History of Guess and Feedback', user_attempts, feedbacks)
    print_history(user_attempts, feedbacks)

    # minor task: this part could be replaced by "function validate"
    if user_attempt == secret_code: 
        print("Congratulations! You guessed the code correctly!")
        break
    
if num_attempts == max_attempts + 1:
    print("Sorry, you've used all your attempts. The secret code is:", secret_code)