import getcode
import validate
import show_result


def validate_input(user_input):
    if len(user_input) != 4:
        return False
    if not user_input.isdigit():
        return False
    return True

def print_history(user_attempts=[], feedbacks=[]):
    if not len(user_attempts):
        print("No history data...")
        return
    for i, (attempt, feedback) in enumerate(zip(user_attempts, feedbacks), start=1):
        print(f"User Attempt {i}: {attempt}, Feedback: {feedback}")

def play():

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
    print("Secret code is generated! Developer mode to show code:", secret_code)

    # Initialize an empty list to store user inputs
    user_attempts = []
    feedbacks = []

    # while loop for 10 attempts
    while num_attempts < max_attempts + 1:
        is_user_input_valid = False

        while is_user_input_valid is False:
            user_input = input("Guess a sequence of four numbers (example: 3102) or enter h to see the history : ")
            # user_input is a string data type!
            if user_input == "h":
                print_history(user_attempts, feedbacks)  
            elif validate_input(user_input):
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
        

        # minor task: this part could be replaced by "function validate"
        if user_attempt == secret_code: 
            print("Congratulations! You win!")
            break
        
    if num_attempts == max_attempts + 1:
        print("Sorry, you've used all your attempts. The secret code is:", secret_code)
        
        
play()