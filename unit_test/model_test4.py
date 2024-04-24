# import unittest
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# this statement adds the parent directory of the current script to the Python path, 
# allowing you to import modules from the parent directory in your script.
from typing import List
import model
from model import validate


# difficulty level: easy but with duplicates
@patch('model.call_api_code')
def test_get_code_easy_infinity(mock_call_api_code):
    # Mocking the return value of call_api_code to return duplicate values multiple times
    # return the value differently in a loop
    mock_call_api_code.side_effect = [[0, 1, 1, 3], [0, 2, 2, 3], [0, 3, 3, 3], [0, 1, 2, 3]]

    result = model.get_code(total_values=4, duplicate=False)
    assert result == [0, 1, 2, 3]

    # Verify that call_api_code was called multiple times
    assert mock_call_api_code.call_count == 4

# difficulty level: easy
@patch('model.call_api_code')
def test_get_code_easy(mock_call_api_code):
    mock_call_api_code.return_value = [0, 1, 2, 3]  # Mocking the return value of call_api_code
    result = model.get_code(total_values=4, duplicate=False)
    assert result == [0, 1, 2, 3]
    
    # Assert that call_api_code was called with max_value=3. ex: call_api_code(3)
    mock_call_api_code.assert_called_once_with(3)  

# difficulty level: medium
@patch('model.call_api_code')
def test_get_code_medium(mock_call_api_code):
    mock_call_api_code.return_value = [0, 1, 1, 7] 

    result = model.get_code(total_values=8, duplicate=True)

    assert result == [0, 1, 1, 7]
    mock_call_api_code.assert_called_once_with(7) 

# difficulty level: hard
@patch('model.call_api_code')
def test_get_code_hard(mock_call_api_code):
    mock_call_api_code.return_value = [0, 5, 5, 9]  

    result = model.get_code(total_values=10, duplicate=True)

    assert result == [0, 5, 5, 9]
    mock_call_api_code.assert_called_once_with(9)  
    
# unit test on validate_input    
def test_validate_input_invalid_length():
    assert model.validate_input("12345", length_input=4) == False
    assert model.validate_input("xsdfs", length_input=4) == False
    assert model.validate_input("5638", length_input=5) == False
    assert model.validate_input("5 6 3 8", length_input=4) == False
    assert model.validate_input(" ", length_input=1) == False

def test_validate_input_invalid_digit():
    assert model.validate_input("5638", length_input=4) == True
    assert model.validate_input("56aa", length_input=4) == False
    assert model.validate_input("bbaa", length_input=4) == False

def test_validate_input_upper_limit():
    assert model.validate_input("10", length_input=2, upper_limit=10) == False
    assert model.validate_input("9", length_input=1, upper_limit=10) == True
    assert model.validate_input("3", length_input=1, upper_limit=3) == False
    assert model.validate_input("2", length_input=1, upper_limit=3) == True
    
    
    
# unit test on validate

def test_validate_full_match():
    secret_code = [0, 1, 3, 5]
    user_attempt = [0, 1, 3, 5]
    number_boolean, position_boolean, correct_number_count, correct_position_count = validate(secret_code, user_attempt)
    assert number_boolean == [True, True, True, True]
    assert position_boolean == [True, True, True, True]
    assert correct_number_count == 4
    assert correct_position_count == 4

def test_validate_no_match():
    secret_code = [0, 1, 3, 5]
    user_attempt = [2, 2, 4, 6]
    number_boolean, position_boolean, correct_number_count, correct_position_count = validate(secret_code, user_attempt)
    assert number_boolean == [False, False, False, False]
    assert position_boolean == [False, False, False, False]
    assert correct_number_count == 0
    assert correct_position_count == 0

def test_validate_partial_match():
    secret_code = [0, 1, 3, 5]
    user_attempt = [0, 2, 4, 6]
    number_boolean, position_boolean, correct_number_count, correct_position_count = validate(secret_code, user_attempt)
    assert number_boolean == [True, False, False, False]
    assert position_boolean == [True, False, False, False]
    assert correct_number_count == 1
    assert correct_position_count == 1

def test_validate_partial_position_match():
    secret_code = [0, 1, 3, 5]
    user_attempt = [2, 2, 1, 1]
    number_boolean, position_boolean, correct_number_count, correct_position_count = validate(secret_code, user_attempt)
    assert number_boolean == [False, False, True, True]
    assert position_boolean == [False, False, False, False]
    assert correct_number_count == 1
    assert correct_position_count == 0

def test_validate_partial_number_match():
    secret_code = [0, 1, 3, 5]
    user_attempt = [0, 1, 5, 6]
    number_boolean, position_boolean, correct_number_count, correct_position_count = validate(secret_code, user_attempt)
    assert number_boolean == [True, True, True, False]
    assert position_boolean == [True, True, False, False]
    assert correct_number_count == 3
    assert correct_position_count == 2
