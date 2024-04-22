def validate_input(user_input: str):
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