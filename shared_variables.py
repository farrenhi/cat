remaining_time = {'time': 0}

input_thread = {'end': False}

# difficulty_config = {'0': 'easy', '1': 'medium', '2': 'hard'}

difficulty_config = {
    '0': {
        'duplicate': False,
        'total_values': 4,
        'announce_level': 0,
        'max_attempts': 15,
    },
    '1': {
        'duplicate': True,
        'total_values': 8, # total is 8, but it would be between 0 and 7.
        'announce_level': 1,
        'max_attempts': 10,
    },
    '2': {
        'duplicate': True,
        'total_values': 10,
        'announce_level': 2,
        'max_attempts': 5,
    }
}

# if we have database system, we will put the following into database.
# keep raw data. Just in case if we need to render them or do different announcement

difficulty_level = []

secret_code = []

user_attempts = []

number_booleans = []

position_booleans = []

counter_correct_numbers = []

feedbacks = []