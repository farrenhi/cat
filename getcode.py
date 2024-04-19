# Module 1
# use the api to randomly get a secret code

# example link from the api website:
# https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new

import requests

def get_code(total_values=4, duplicate=False):
    '''
    This function will use external API to randomly select 4 secret codes.
    
    Input:
    the default values for random selection is only 4 numbers. Just for easy level of the game
    the default setting for duplicate is False for easy level.
    
    Output: 4 digit of secret code. data type: array
    '''
    max_value = 0 + total_values - 1 # including 0!
    
    if duplicate is True:
        numbers = call_api_code(max_value)
    else:
        find_no_duplicate = False
        while not find_no_duplicate:
            # future task: infinity loop or too many requests to external API?
            numbers = call_api_code(max_value)
            numbers_set = set(numbers)
            if len(numbers_set) == 4:
                find_no_duplicate = True
    
    # print(numbers)
    return numbers

def call_api_code(max_value):
    url = f"https://www.random.org/integers/?num=4&min=0&max={max_value}&col=1&base=10&format=plain&rnd=new"

    response = requests.get(url)
    
    if response.status_code == 200:
        numbers = response.text.split("\n")[:-1]  # Split the text by newline and remove the last empty element
        numbers = [int(num) for num in numbers]   # Convert the text numbers to integers
        # print("API result:", numbers)
        return numbers 
    else:
        print("Failed to fetch numbers. Status code:", response.status_code)


# get_code(duplicate=False)