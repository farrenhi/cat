import getcode

print("Hello, are you ready for the game?")

# the follow is to be done.
# input the difficulty level: total_values, duplicates...

secret_code = getcode.get_code(total_values=4, duplicate=False)
# Future task: this would take a wile to generate non duplicate secret code

print("Secret code is generated!", secret_code)