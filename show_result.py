# the code announces the result based on the validation.py, two arrays of boolean
# based on "difficulty_level", it would decide to reveal full info or just partial
# difficulty level: easy, medium, hard
# easy, 0: full info
# medium, 1: as requested in the assignment. no precise 
# hard, 2: only incorrect or correct (no number or position info)

def announce(user_attempt, number_boolean, position_boolean, \
     counter_correct_number, difficulty_level=1):
    
    number_true_count = number_boolean.count(True)
    position_true_count = position_boolean.count(True)
    
    if difficulty_level == 0: # easy
        if number_true_count == len(number_boolean) and position_true_count == len(position_boolean):
            announce_statement = "All good. You win!"
        else:
            announce_statement = explain(number_boolean, position_boolean, user_attempt)
    
    elif difficulty_level == 1: # medium
        if number_true_count == 0:
            announce_statement = "All incorrect... Keep guessing!"
        elif number_true_count == len(number_boolean) and position_true_count == len(position_boolean):
            announce_statement = "All good. You win!"
        else:
            # future task: how to make the plural correct... currently, (s) would be ok!

            announce_statement = f"{counter_correct_number} correct number(s) and {position_true_count} correct location(s)."
    
    elif difficulty_level == 2: # hard
        if number_true_count == len(number_boolean) and position_true_count == len(position_boolean):
            announce_statement = "All good. You win!"
        else:
            announce_statement = "Incorrect... Keep guessing!"            
    else:
        print("wrong input for difficulty level!")
        
    print(announce_statement)

# number_boolean=[True, True, True, True], \
    # position_boolean=[False, False, False, True]

def explain(number_boolean, position_boolean, user_attempt):
    statement = []
    print("Correctness:", position_boolean)
    for index, value in enumerate(position_boolean):
        if value is True:
            statement.append(f"Position {index} is correct. ")
        else:
            if number_boolean[index] is False:
                statement.append(f"Number {user_attempt[index]} is not in the code. ")
    
    return ''.join(statement)

# announce()