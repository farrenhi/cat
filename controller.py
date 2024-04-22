import getcode
import validate
import show_result
import shared_variables
import core_logic
import view_command_line
import model

def play():
    # future task: need to do a figuration setting and load it into play function. currently, just put inside...

    ### game configuration
    difficulty_level = 1
    duplicate = True
    total_values = 8 # total is 8, but it would be between 0 and 7.
    max_attempts = 10
    ###

    #####################
    num_attempts = 1

    secret_code = getcode.get_code(total_values, duplicate)
    
    view_command_line.present_to_user("Hello, are you ready for the game?")

    # Future task: this would take a wile to generate non duplicate secret code
    # how to solve this long wait?

    view_command_line.present_to_user(f"Secret code ready! In testing: {secret_code}")

    # Initialize an empty list to store user inputs
    user_attempts = []
    feedbacks = []

    # while loop for 10 attempts
    while num_attempts < max_attempts + 1:
        is_user_input_valid = False

        while is_user_input_valid is False:
            view_command_line.present_to_user(f"remaining time: {shared_variables.remaining_time['time']} second(s)")

            user_input = view_command_line.ask_user_guess()
            # user_input is a string data type!
            
            if user_input == "h":
                view_command_line.print_history(user_attempts, feedbacks)
            elif model.validate_input(user_input):
                is_user_input_valid = True
            else:
                view_command_line.present_to_user("Please input 4 digit of numbers.")

        user_attempt = [int(digit) for digit in user_input] # convert string into integer
        # print(f"Your Guess Attempt {num_attempts}: ", user_attempt)
        view_command_line.present_to_user(f"Your Guess Attempt {num_attempts}: {user_attempt}")
        
        num_attempts += 1

        user_attempts.append(user_attempt)
        
        number_boolean, position_boolean, counter_correct_number = \
            validate.validate(secret_code=secret_code, user_attempt=user_attempt)

        feedback = show_result.announce(user_attempt, number_boolean, position_boolean, \
            counter_correct_number, difficulty_level)

        view_command_line.present_to_user(f"Feedback: {feedback}")
      
        feedbacks.append(feedback)
        
        view_command_line.present_to_user(f"Number of guesses remaining: {max_attempts - num_attempts + 1}")
        view_command_line.present_to_user('--------------------------')
        

        # minor task: this part could be replaced by "function validate"
        if user_attempt == secret_code: 
            view_command_line.present_to_user("Congratulations! You win!")
            shared_variables.input_thread['end'] = True
            break
        
    if num_attempts == max_attempts + 1:
        shared_variables.input_thread['end'] = True
        view_command_line.present_to_user(f"Sorry, you've used all your attempts. The secret code is: {secret_code}")