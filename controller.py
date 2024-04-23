import shared_variables
import view_command_line
import model

def play():
    # future task: need to do a figuration setting and load it into play function. currently, just put inside...

    view_command_line.present_to_user("Hello, ready for the game?")
    difficulty_level = get_valid_level()
    model.write_to_database(shared_variables.difficulty_level, difficulty_level)

    # game configuration
    duplicate = shared_variables.difficulty_config[difficulty_level]['duplicate']
    total_values = shared_variables.difficulty_config[difficulty_level]['total_values']
    max_attempts = shared_variables.difficulty_config[difficulty_level]['max_attempts']
    announce_level = shared_variables.difficulty_config[difficulty_level]['announce_level']
    
    num_attempts = 1

    secret_code = model.get_code(total_values, duplicate)
    model.write_to_database(shared_variables.secret_code, secret_code)
    view_command_line.present_to_user(f"Secret code ready! In testing: {secret_code}")
    # Future task: randomly, might take too long to generate non duplicate secret code

    # while loop for 10 attempts
    while num_attempts < max_attempts + 1:
        
        user_attempt = get_valid_attempt(total_values)
        model.write_to_database(shared_variables.user_attempts, user_attempt)
        view_command_line.present_to_user(f"Your Guess Attempt {num_attempts}: {user_attempt}")
        
        num_attempts += 1
        
        number_boolean, position_boolean, counter_correct_number, counter_position_boolean = \
            model.validate(secret_code=secret_code, user_attempt=user_attempt)
        model.write_to_database(shared_variables.number_booleans, number_boolean)
        model.write_to_database(shared_variables.position_booleans, position_boolean)
        model.write_to_database(shared_variables.counter_correct_numbers, counter_correct_number)
        model.write_to_database(shared_variables.counter_position_booleans, counter_position_boolean)

        feedback = model.announce(user_attempt, number_boolean, position_boolean, \
            counter_correct_number, announce_level)
        model.write_to_database(shared_variables.feedbacks, feedback)
        view_command_line.present_to_user(f"Feedback: {feedback}")
        
        shared_variables.input_thread['attempts_left'] = max_attempts - num_attempts + 1
        attempts_left = shared_variables.input_thread['attempts_left']
        view_command_line.present_to_user(f"Number of guesses remaining: {attempts_left}")
        view_command_line.present_to_user('--------------------------')
        
        # Win! Add function calculate_score here
        if position_boolean.count(True) == len(secret_code):
            # this switch is for timer (concurrency. multi-threading)  
            shared_variables.input_thread['end'] = True
            score = model.calculate_score(shared_variables.difficulty_config[difficulty_level],
                                          attempts_left, shared_variables.remaining_time['time'], True,
                                          shared_variables.counter_correct_numbers,
                                          shared_variables.counter_position_booleans
                                          )
            view_command_line.present_to_user(f"Your score: {score}")
            break
     
    # Loose! Add function calculate_score here
    # Add function calculate_score to timer side!
    if num_attempts == max_attempts + 1:
        shared_variables.input_thread['end'] = True
        view_command_line.present_to_user(f"Sorry, you've used all your attempts. The secret code is: {secret_code}")
        
        score = model.calculate_score(shared_variables.difficulty_config[difficulty_level],
                                    attempts_left, shared_variables.remaining_time['time'], False,
                                    shared_variables.counter_correct_numbers,
                                    shared_variables.counter_position_booleans
                                    )
        view_command_line.present_to_user(f"Your score: {score}")
     
def get_valid_attempt(total_values) -> list:
    '''Get valid attempt guess input from user
    '''
    is_user_input_valid = False
    while is_user_input_valid is False:
        view_command_line.present_to_user(f"remaining time: {shared_variables.remaining_time['time']} second(s)")

        user_input = view_command_line.ask_user_guess(total_values)
        # user_input is a string data type!
        
        if user_input == "h":
            view_command_line.print_history(shared_variables.user_attempts, shared_variables.feedbacks)
        elif model.validate_input(user_input, 4): # 4 is hard coded here. Q: avoid this?
            is_user_input_valid = True
            user_attempt = [int(digit) for digit in user_input] # convert string into integer
        else:
            view_command_line.present_to_user("Please input 4 digit of numbers.")

    return user_attempt

def get_valid_level() -> int:
    '''Get valid user input for difficulty level form view layer
    '''
    is_level_valid = False
    while not is_level_valid:
        level_input = view_command_line.ask_user_difficulty()
        if model.validate_input(level_input, 1, upper_limit=3):
            is_level_valid = True
        else:
            view_command_line.present_to_user("Please enter one number between 0 and 2.")
    return level_input
        