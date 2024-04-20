import getcode
import validate
import show_result

print("Hello, are you ready for the game?")

# the follow is to be done.
# input the difficulty level: total_values, duplicates...

### user input
user_attempt = [3, 2, 0, 1]
difficulty_level = 1
duplicate = True
total_values = 8
###


secret_code = getcode.get_code(total_values, duplicate)
# Future task: this would take a wile to generate non duplicate secret code

print("Secret code is generated!", secret_code)

number_boolean, position_boolean, counter_correct_number = \
    validate.validate(secret_code=secret_code, user_attempt=user_attempt)

show_result.announce(user_attempt, number_boolean, position_boolean, \
    counter_correct_number, difficulty_level)