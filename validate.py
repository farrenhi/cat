# this function is to validate if the user's attempt is correct or not
# the code will specify if correct number and if correct position (for full visibility)
# based on the difficulty level, the code would choose what to reveal or not
# this code would provide the full visibility of the info (number and position)

def validate(secret_code=[1, 2, 3, 0], user_attempt=[2, 1, 3, 0]):
    '''
    The validate function would check the secret_code and user_attempt.
    Input: two arrays of number. secret_code and user_attempt
    Output: two arrays of booleans. number correctness and position correctness 
    
    '''
    number_boolean = []
    position_boolean = []
    secret_code_set = set(secret_code)
    for index, value in enumerate(user_attempt):
        if value in secret_code_set:
            number_boolean.append(True)
            # future task: should I isolate this part? seems like not that complicated!
            if value == secret_code[index]:
                position_boolean.append(True)
            else:
                position_boolean.append(False)
        else: # if value is not in secret_set, then position is also False
            number_boolean.append(False)
            position_boolean.append(False)
    
    print("number_boolean:", number_boolean)
    print("position_boolean", position_boolean)
    return number_boolean, position_boolean

