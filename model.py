# Module 1
# use the api to randomly get a secret code

# example link from the api website:
# https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new

# future task: one digit per request!
from typing import List
import requests
import shared_variables

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