# the code announces the result based on the validation.py, two arrays of boolean
# based on "difficulty_level", it would decide to reveal full info or just partial
# difficulty level: easy, medium, hard
# easy, 0: full info
# medium, 1: as requested in the assignment. no precise 
# hard, 2: only incorrect or correct (no number or position info)

def announce(number_boolean=[True, True, True, True], \
    position_boolean=[False, False, False, True], difficulty_level=1):
    
    if difficulty_level == 0: # easy
        pass
    elif difficulty_level == 1: # medium
        number_true_count = number_boolean.count(True)
        position_true_count = position_boolean.count(True)
        if number_true_count == 0:
            announce_statement = "All incorrect... Keep guessing!"
        elif number_true_count == len(number_boolean) and position_true_count == len(position_boolean):
            announce_statement = "All good. You win!"
        else:
            # future task: how to make the plural correct... currently, (s) would be ok!
            announce_statement = f"{number_true_count} correct number(s) and {position_true_count} correct location(s)."
    elif difficulty_level == 2: # hard
        pass
    else:
        print("wrong input for difficulty level!")
        
    print(announce_statement)
        
announce()