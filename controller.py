# import shared_variables
import view_command_line
import model
from model import Player
import threading
import time

# Q: timer class should be moved to model.py. (future task)
class Timer:
    def __init__(self, duration, callback, player):
        self.duration = duration
        self.callback = callback
        self.player = player
        self.player.time_left = self.duration
        self._is_running = False
        self.start_time = None
        self.stop_time = None
        self._stop_event = threading.Event()

    def start(self):
        self._is_running = True
        self.start_time = time.time()
        threading.Thread(target=self._run_timer).start()

    def stop(self):
        self._is_running = False
        self.stop_time = time.time()
        if self.player.win:
            self.player.time_left = self.duration - int(self.stop_time - self.start_time)
        self.callback(self.player)
        self._stop_event.set()
        # want to terminate the thread just call: thread.event.set()

    def _run_timer(self):
        # time.sleep(self.duration)  # Simulate timer running for 'duration' seconds
        # if self._is_running:
        #     self.callback(self.player)
        while not self._stop_event.is_set() and time.time() - self.start_time < self.duration:
            time.sleep(1)
            self.player.time_left = self.duration - int(time.time() - self.start_time)

        if not self._stop_event.is_set():
            self.callback(self.player)

class Controller:
    def __init__(self, view, players, turn_duration):
        self.view = view
        self.players = players
        self.turn_duration = turn_duration

    def run(self):
        for player in self.players:
            self.play(player)

    # Q: how to do unit test? Now, it is too complicated. 
    # Should I make this function into more blocks firstly?
    
    def play(self, player):
        name = self.view.ask_user_name()
        if name:
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

        # start timer
        self.view.present_to_user(f"{player.name}, your turn! Time starts now.")
        timer = Timer(self.turn_duration, self.on_timer_end, player)
        timer.start()
        
        # Ask user if they would like to exchange 3 attempts for a single digit of the secret code.
        trade = self.view.ask_user_trade()
        if trade is not None:
            if trade == "1":
                max_attempts -= 3
                self.view.present_to_user(f"First digit is {secret_code[0]}!")                

        player.attempts_left = max_attempts
        
        # while loop for 10 attempts
        while not player.end and num_attempts < max_attempts + 1:
            
            user_attempt = self.get_valid_attempt(player)
            if not user_attempt:
                break
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
                player.win = True
                timer.stop()
                # this switch is for timer (concurrency. multi-threading)  
                player.calculate_score()
                self.view.present_to_user(f"Your score: {player.score}")
                return
        
        # Loose! Add function calculate_score here
        # Add function calculate_score to timer side!
        timer.stop()

        if num_attempts == max_attempts + 1:
            self.view.present_to_user(f"Sorry, you've used all your attempts. The secret code is: {player.secret_code}")
            player.calculate_score()
            self.view.present_to_user(f"Your score: {player.score}")
        elif num_attempts == 1:
            self.view.present_to_user(f"Your score: 0")
        else:
            self.view.present_to_user("Time is up!")
            player.calculate_score()
            self.view.present_to_user(f"Your score: {player.score}")
            
    def on_timer_end(self, player):
        # self.view.present_to_user("Time's up!")
        player.end = True
        
    def get_valid_attempt(self, player) -> list:
        '''Get valid attempt guess input from user
        '''
        is_user_input_valid = False
        user_attempt = None
        while not player.end and not is_user_input_valid:
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

    number_player = input("Please enter number of player(s)? (1 or 2) ")
    
    view = view_command_line.View()
    player1 = Player('Player1')
    controller = Controller(view, [player1], turn_duration=10)
    
    if number_player == "2":
        controller.players.append(Player('Player2'))
    
    controller.run()

    for player in controller.players:
        print(f"{player.name}: {player.score}")
        

