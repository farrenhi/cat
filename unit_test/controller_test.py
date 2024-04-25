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
    # mock_ask_user_difficulty.return_value = '4'  # Mock user input
    # mock_validate_input.return_value = False  # Mock validation result

    mock_ask_user_difficulty.side_effect = ['4', '5', '6', '2']  # Mock user input
    mock_validate_input.side_effect = [False, False, False, True]  # Mock validation result
    
    view = view_command_line.View()
    player1 = model.Player('Player1')
    instance = controller.Controller(view, [player1], turn_duration=10)
    # Call the function
    result = instance.get_valid_level()

    assert result == '2'  # Ensure the returned value is correct

    assert mock_ask_user_difficulty.call_count == 4
    
    # Ensure validate_input was called with the correct arguments  
    #                    validate_input(level_input, 1, upper_limit=3)
    mock_validate_input.assert_any_call('4', 1, upper_limit=3) 
    mock_validate_input.assert_any_call('5', 1, upper_limit=3)
    mock_validate_input.assert_any_call('6', 1, upper_limit=3)
    
    # Ensure present_to_user was called with the correct message
    # count display times of this message: "Please enter one number between 0 and 2."   
    assert mock_present_to_user.call_count == 3