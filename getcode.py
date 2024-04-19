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
    
    max_value = 0 + total_values

    url = f"https://www.random.org/integers/?num=4&min=0&max={max_value}&col=1&base=10&format=plain&rnd=new"

    response = requests.get(url)
    if response.status_code == 200:
        numbers = response.text.split("\n")[:-1]  # Split the text by newline and remove the last empty element
        numbers = [int(num) for num in numbers]   # Convert the text numbers to integers
        set_numbers = set(numbers)
        # print("Random numbers:", numbers)
        # print("Set of numbers:", set_numbers)
        
        # duplicate check and recursion
        # future task: 
        # 1. check if logic is ok (unit test?) and see if we should isolate this as a function check
        # 2. what if it keeps getting duplicates? infinity loop? (but it is like throwing coins!)
        if not duplicate and len(set_numbers) < 4:
            get_code(total_values, duplicate)
        else:
            return numbers
    else:
        print("Failed to fetch numbers. Status code:", response.status_code)


# get_code(duplicate=False)