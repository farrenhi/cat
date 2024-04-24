# import unittest
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# this statement adds the parent directory of the current script to the Python path, 
# allowing you to import modules from the parent directory in your script.

import model


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