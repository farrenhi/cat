# import unittest
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import model


@patch('model.call_api_code')
def test_get_code_no_duplicate(mock_call_api_code):
    mock_call_api_code.return_value = [0, 1, 2, 3]  # Mocking the return value of call_api_code
    result = model.get_code(total_values=4, duplicate=False)
    assert result == [0, 1, 2, 3]

@patch('your_module.call_api_code')
def test_get_code_with_duplicate(mock_call_api_code):
    mock_call_api_code.return_value = [0, 1, 1, 3]  # Mocking the return value of call_api_code

    result = model.get_code(total_values=4, duplicate=True)

    assert result == [0, 1, 1, 3]
    mock_call_api_code.assert_called_once_with(3)  # Assert that call_api_code was called with max_value=3
