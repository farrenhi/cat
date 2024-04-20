import getcode
import validate
import show_result

print("Hello, are you ready for the game?")

# the follow is to be done.
# input the difficulty level: total_values, duplicates...

### user input
difficulty_level = 1
duplicate = True
total_values = 8
###




#####################
# Initialize the number of attempts and maximum attempts
num_attempts = 1
max_attempts = 10

# Define the secret code
secret_code = getcode.get_code(total_values, duplicate)

# Future task: this would take a wile to generate non duplicate secret code
# how to solve this long wait?
print("Secret code is generated!", secret_code)

# Initialize an empty list to store user inputs
user_attempts = []

# Start the while loop
while num_attempts < max_attempts + 1:
    # Ask the user to input a sequence of four numbers
    user_input = input("Guess a sequence of four numbers (example: 3102): ")

    # Convert the input string into a list of integers
    user_attempt = [int(digit) for digit in user_input]
    print(f"Your Guess Attempt {num_attempts}:", user_attempt)

    # Increment the number of attempts
    num_attempts += 1

    # Append the user attempt to the list of attempts
    user_attempts.append(user_attempt)
    
    number_boolean, position_boolean, counter_correct_number = \
        validate.validate(secret_code=secret_code, user_attempt=user_attempt)

    show_result.announce(user_attempt, number_boolean, position_boolean, \
        counter_correct_number, difficulty_level)
    
    print('--------------------------')

    # Check if the user's attempt matches the secret code
    if user_attempt == secret_code:
        print("Congratulations! You guessed the code correctly!")
        break  # Exit the loop if the code is guessed correctly

# Check if the user has exhausted all attempts
if num_attempts == max_attempts + 1:
    print("Sorry, you've used all your attempts. The secret code is:", secret_code)
