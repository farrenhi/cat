# import shared_variables
import view_command_line
import model
from model import Player

class Controller:
    def __init__(self):
        self.view = view_command_line.View()
        # self.model = model

        self.players = [Player('Player1')] 
        # future task: ask View layer for the user's name and put it here
    
    def run(self):
        for player in self.players:
            self.play(player)

    def play(self, player):
        name = self.view.ask_user_name()
        if name is not None:
            player.update(name=name)

        self.view.present_to_user(f"Hello {player.name}, ready for the game?")
        difficulty_level = self.get_valid_level()
        # model.write_to_database(shared_variables.difficulty_level, difficulty_level)
        player.update(difficulty_level=difficulty_level)
        
        # game configuration
        duplicate = player.difficulty_config[player.difficulty_level]['duplicate']
        total_values = player.difficulty_config[player.difficulty_level]['total_values']
        max_attempts = player.difficulty_config[player.difficulty_level]['max_attempts']
        announce_level = player.difficulty_config[player.difficulty_level]['announce_level']
        
        num_attempts = 1

        secret_code = model.get_code(total_values, duplicate)
        # model.write_to_database(shared_variables.secret_code, secret_code)
        player.update(secret_code=secret_code)
        self.view.present_to_user(f"Secret code ready! In testing: {secret_code}")
        # Future task: randomly, might take too long to generate non duplicate secret code

        # while loop for 10 attempts
        while num_attempts < max_attempts + 1:
            
            user_attempt = self.get_valid_attempt(player)
            # model.write_to_database(shared_variables.user_attempts, user_attempt)
            player.user_attempts.append(user_attempt)
            self.view.present_to_user(f"Your Guess Attempt {num_attempts}: {user_attempt}")
            
            num_attempts += 1
            
            number_boolean, position_boolean, counter_correct_number, counter_position_boolean = \
                model.validate(secret_code=secret_code, user_attempt=user_attempt)
                
            # model.write_to_database(shared_variables.number_booleans, number_boolean)
            # model.write_to_database(shared_variables.position_booleans, position_boolean)
            # model.write_to_database(shared_variables.counter_correct_numbers, counter_correct_number)
            # model.write_to_database(shared_variables.counter_position_booleans, counter_position_boolean)
            
            player.number_booleans.append(number_boolean)
            player.position_booleans.append(position_boolean)
            player.counter_correct_numbers.append(counter_correct_number)
            player.counter_position_booleans.append(counter_position_boolean)
            
            feedback = model.announce(user_attempt, number_boolean, position_boolean, \
                counter_correct_number, announce_level)
            # model.write_to_database(shared_variables.feedbacks, feedback)
            player.feedbacks.append(feedback)
            self.view.present_to_user(f"Feedback: {feedback}")
            
            # shared_variables.input_thread['attempts_left'] = max_attempts - num_attempts + 1
            player.attempts_left = max_attempts - num_attempts + 1
            # attempts_left = shared_variables.input_thread['attempts_left']
            
            self.view.present_to_user(f"Number of guesses remaining: {player.attempts_left}")
            self.view.present_to_user('--------------------------')
            
            # Win! Add function calculate_score here
            if position_boolean.count(True) == len(secret_code):
                # this switch is for timer (concurrency. multi-threading)  
                player.end, player.win = True, True
                player.calculate_score()

                self.view.present_to_user(f"Your score: {player.score}")
                break
        
        # Loose! Add function calculate_score here
        # Add function calculate_score to timer side!
        if num_attempts == max_attempts + 1:
            player.end = True
            player.calculate_score()
            self.view.present_to_user(f"Sorry, you've used all your attempts. The secret code is: {player.secret_code}")
            self.view.present_to_user(f"Your score: {player.score}")
        
    def get_valid_attempt(self, player) -> list:
        '''Get valid attempt guess input from user
        '''
        is_user_input_valid = False
        while is_user_input_valid is False:
            self.view.present_to_user(f"remaining time: {player.time_left} second(s)")

            total_values = player.difficulty_config[player.difficulty_level]['total_values']
            user_input = self.view.ask_user_guess(total_values)
            # user_input is a string data type!
            
            if user_input == "h":
                self.view.print_history(player.user_attempts, player.feedbacks)
            elif model.validate_input(user_input, 4): # 4 is hard coded here. Q: avoid this?
                is_user_input_valid = True
                user_attempt = [int(digit) for digit in user_input] # convert string into integer
            else:
                self.view.present_to_user("Please input 4 digit of numbers.")

        return user_attempt

    def get_valid_level(self) -> int:
        '''Get valid user input for difficulty level form view layer
        '''
        is_level_valid = False
        while not is_level_valid:
            level_input = self.view.ask_user_difficulty()
            if model.validate_input(level_input, 1, upper_limit=3):
                is_level_valid = True
            else:
                self.view.present_to_user("Please enter one number between 0 and 2.")
        return level_input

# debug for class instantiation
if __name__ == "__main__":

    number_player = input("Please enter number of players? (1 or 2) ")
    controller = Controller()
    
    if number_player == "2":
        controller.players.append(Player('Player2'))
    
    controller.run()
    for player in controller.players:
        print(f"{player.name}: {player.score}")