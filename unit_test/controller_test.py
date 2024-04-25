from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import controller
import model
import view_command_line


# check if this unit test is simple enough or too complicated (involves other classes...)
@patch('model.validate_input')
@patch('view_command_line.View.ask_user_difficulty')
@patch('view_command_line.View.present_to_user')
def test_get_valid_level_valid_input(mock_present_to_user, mock_ask_user_difficulty, mock_validate_input):
    mock_ask_user_difficulty.return_value = '1'  # Mock user input
    mock_validate_input.return_value = True  # Mock validation result

    view = view_command_line.View()
    player1 = model.Player('Player1')
    instance = controller.Controller(view, [player1], turn_duration=10)
    # Call the function
    result = instance.get_valid_level()

    # Assertions
    assert result == '1'  # Ensure the returned value is correct
    mock_ask_user_difficulty.assert_called_once()  # Ensure ask_user_difficulty was called
    mock_validate_input.assert_called_once_with('1', 1, upper_limit=3)  # Ensure validate_input was called with the correct arguments

@patch('model.validate_input')
@patch('view_command_line.View.ask_user_difficulty')
@patch('view_command_line.View.present_to_user')
def test_get_valid_level_invalid_input(mock_present_to_user, mock_ask_user_difficulty, mock_validate_input):
    mock_ask_user_difficulty.return_value = '4'  # Mock user input
    mock_validate_input.return_value = False  # Mock validation result

    view = view_command_line.View()
    player1 = model.Player('Player1')
    instance = controller.Controller(view, [player1], turn_duration=10)
    # Call the function
    result = instance.get_valid_level()


    assert result == '4'  # Ensure the returned value is correct
    mock_ask_user_difficulty.assert_called_once()  # Ensure ask_user_difficulty was called
    mock_validate_input.assert_called_once_with('4', 1, upper_limit=3)  # Ensure validate_input was called with the correct arguments
    mock_present_to_user.assert_called_once_with("Please enter one number between 0 and 2.")  # Ensure present_to_user was called with the correct message