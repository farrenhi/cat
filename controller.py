import shared_variables
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

    view_command_line.present_to_user("Hello, ready for the game?")

    secret_code = model.get_code(total_values, duplicate)
    model.write_to_database(shared_variables.secret_code, secret_code)
    view_command_line.present_to_user(f"Secret code ready! In testing: {secret_code}")
    # Future task: randomly, might take too long to generate non duplicate secret code

    # while loop for 10 attempts
    while num_attempts < max_attempts + 1:
        
        user_attempt = get_valid_attempt()
        model.write_to_database(shared_variables.user_attempts, user_attempt)
        view_command_line.present_to_user(f"Your Guess Attempt {num_attempts}: {user_attempt}")
        
        num_attempts += 1
        
        number_boolean, position_boolean, counter_correct_number = \
            model.validate(secret_code=secret_code, user_attempt=user_attempt)
        model.write_to_database(shared_variables.number_booleans, number_boolean)
        model.write_to_database(shared_variables.position_booleans, position_boolean)
        model.write_to_database(shared_variables.counter_correct_numbers, counter_correct_number)

        feedback = model.announce(user_attempt, number_boolean, position_boolean, \
            counter_correct_number, difficulty_level)
        model.write_to_database(shared_variables.feedbacks, feedback)
        view_command_line.present_to_user(f"Feedback: {feedback}")
        
        view_command_line.present_to_user(f"Number of guesses remaining: {max_attempts - num_attempts + 1}")
        view_command_line.present_to_user('--------------------------')
        
        if position_boolean.count(True) == len(secret_code):
            # this switch is for timer (concurrency. multi-threading)  
            shared_variables.input_thread['end'] = True
            break
        
    if num_attempts == max_attempts + 1:
        shared_variables.input_thread['end'] = True
        view_command_line.present_to_user(f"Sorry, you've used all your attempts. The secret code is: {secret_code}")
     
def get_valid_attempt() -> list:
    '''Get valid attempt guess input from user
    '''
    is_user_input_valid = False
    while is_user_input_valid is False:
        view_command_line.present_to_user(f"remaining time: {shared_variables.remaining_time['time']} second(s)")

        user_input = view_command_line.ask_user_guess()
        # user_input is a string data type!
        
        if user_input == "h":
            view_command_line.print_history(shared_variables.user_attempts, shared_variables.feedbacks)
        elif model.validate_input(user_input):
            is_user_input_valid = True
            user_attempt = [int(digit) for digit in user_input] # convert string into integer
        else:
            view_command_line.present_to_user("Please input 4 digit of numbers.")

    return user_attempt