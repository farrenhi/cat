from typing import List, Tuple
import requests
import shared_variables

def validate(secret_code: List[int], user_attempt: List[int]) -> Tuple[List[bool], List[bool], int]:
    '''Validate secret code and user attempt. Then, output validation result.
    # this function is to validate if the user's attempt is correct or not
    # the code will specify correct number and correct position (for full visibility)
    # based on the difficulty level, the other function would choose what to reveal or not
    # this function would provide the full visibility of the info (number and position)
    
    >>> validate([0, 1, 3, 5], [0, 1, 3, 5])
    ([True, True, True, True], [True, True, True, True], 4)
    
    >>> validate([0, 1, 3, 5], [2, 2, 4, 6])
    ([False, False, False, False], [False, False, False, False], 0)
    
    >>> validate([0, 1, 3, 5], [0, 2, 4, 6])
    ([True, False, False, False], [True, False, False, False], 1)
    
    >>> validate([0, 1, 3, 5], [2, 2, 1, 1])
    ([False, False, True, True], [False, False, False, False], 1)
    
    >>> validate([0, 1, 3, 5], [0, 1, 5, 6])
    ([True, True, True, False], [True, True, False, False], 3)
    '''
    
    number_boolean = []
    position_boolean = []
    counter_correct_number = 0

    secret_code_set = set(secret_code)
    for index, value in enumerate(user_attempt):
        if value in secret_code_set:
            
            # future task: how to combine counter_correct_number here inside the loop!
            # this would work only on sorted array!
            # if index > 0 and user_attempt[index] == user_attempt[index - 1]:
            #     pass
            # else:
            #     counter_correct_number += min(user_attempt.count(value), secret_code.count(value))
            
            number_boolean.append(True)
            # future task: should I isolate this part? seems like not that complicated!
            if value == secret_code[index]:
                position_boolean.append(True)
            else:
                position_boolean.append(False)
        else: # if value is not in secret_set, then position is also False
            number_boolean.append(False)
            position_boolean.append(False)
    
    # future task: could we combine the following loop with the above?     
    for number in secret_code_set:
        counter_correct_number += min(user_attempt.count(number), secret_code.count(number))

    return number_boolean, position_boolean, counter_correct_number


def announce(user_attempt: List[int], 
             number_boolean: List[bool], 
             position_boolean: List[bool], 
             counter_correct_number: int, 
             difficulty_level: int = 1) -> str:
    '''Announce the result based on the validation result
    # based on "difficulty_level", it would decide to reveal full info or just partial
    # difficulty level: easy, medium, hard
    # easy, 0: full info
    # medium, 1: as requested in the assignment. 
    # hard, 2: only incorrect or correct info (no number or position info)
    '''
    
    number_true_count = number_boolean.count(True)
    position_true_count = position_boolean.count(True)
    
    if difficulty_level == 0: # easy
        if number_true_count == len(number_boolean) and position_true_count == len(position_boolean):
            announce_statement = "You win!"
        else:
            announce_statement = explain(number_boolean, position_boolean, user_attempt)
    
    elif difficulty_level == 1: # medium
        if number_true_count == 0:
            announce_statement = "All incorrect... Keep guessing!"
        elif number_true_count == len(number_boolean) and position_true_count == len(position_boolean):
            announce_statement = "You win!"
        else:
            # future task: how to make the plural correct... currently, (s) would be ok!
            announce_statement = f"{counter_correct_number} correct number(s) and {position_true_count} correct location(s)."
    
    elif difficulty_level == 2: # hard
        if number_true_count == len(number_boolean) and position_true_count == len(position_boolean):
            announce_statement = "You win!"
        else:
            announce_statement = "Incorrect... Keep guessing!"            
    else:
        print("wrong input for difficulty level!")
        
    return announce_statement

def explain(number_boolean: List[bool], 
            position_boolean: List[bool], 
            user_attempt: List[int]) -> str:
    statement = []
    print("Correctness:", position_boolean)
    for index, value in enumerate(position_boolean):
        if value is True:
            statement.append(f"Position {index} is correct. ")
        else:
            if number_boolean[index] is False:
                statement.append(f"Number {user_attempt[index]} is not in the code. ")
    
    return ''.join(statement)


# def write_to_database(user_attempt: List[int]) -> None:
def write_to_database(dataset: list, data) -> None:
    '''Write data to a database. 
    Command Line Interface version is just a list to store data in shared_variables.py 
    '''
    dataset.append(data)
    return
   

def validate_input(user_input: str) -> bool:
    '''validate if the input format is good
    >>> validate_input("12345")
    False
    
    >>> validate_input("xsdfs")
    False
    
    >>> validate_input("5638")
    True
    
    >>> validate_input("5 6 3 8")
    False
    
    >>> validate_input(" ")
    False
    '''
    
    if len(user_input) != 4:
        return False
    if not user_input.isdigit():
        return False
    return True

def get_code(total_values: int = 4, duplicate: bool = False) -> list:
    '''This function will use external API to randomly select 4 secret codes. 
    the default values for random selection is only 4 numbers. Just for easy level of the game
    the default setting for duplicate is False for easy level.
    
    Future task: how to write doctest on this function?
    
    '''
    max_value = 0 + total_values - 1 # including 0!
    
    if duplicate is True:
        numbers = call_api_code(max_value)
    else:
        find_no_duplicate = False
        while not find_no_duplicate:
            # future task: 
            # 1. infinity loop or too many requests to external API?
            # 2. time bottleneck: or try a different external API for non duplicates?
            numbers = call_api_code(max_value)
            numbers_set = set(numbers)
            if len(numbers_set) == 4:
                find_no_duplicate = True
    
    # print(numbers)
    return numbers

def call_api_code(max_value: int) -> list:
    '''Call external API to get random number
    '''
    url = f"https://www.random.org/integers/?num=4&min=0&max={max_value}&col=1&base=10&format=plain&rnd=new"

    response = requests.get(url)
    
    if response.status_code == 200:
        numbers = response.text.split("\n")[:-1]  # Split the text by newline and remove the last empty element
        numbers = [int(num) for num in numbers]   # Convert the text numbers to integers
        # print("API result:", numbers)
        return numbers 
    else:
        print("Failed to fetch numbers. Status code:", response.status_code)