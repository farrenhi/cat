from typing import List

# Q: unit test on view?
class View:
    def ask_user_name(self):
        name = input("What is your name? ")
        return name
    
    def ask_user_trade(self):
        print("Do you want to exchange 2 attempts to reveal a digit of the secret code?")
        answer = input("Enter 1 for yes or 2 for no: ")
        return answer

    def print_history(self, user_attempts: List[int] = [], feedbacks: List[str] = []) -> None:
        if not len(user_attempts):
            print("No history data...")
        
        for i, (attempt, feedback) in enumerate(zip(user_attempts, feedbacks), start=1):
            print(f"User Attempt {i}: {attempt}, Feedback: {feedback}")

    def present_to_user(self, statement: str = None) -> None:
        if statement:
            print(statement)

    def ask_user_guess(self, total_values) -> str:
        user_input = input(f"Guess four numbers between 0 and {total_values - 1} (ex: 3102) or enter h for history: ")
        return user_input

    # need to valid user input
    def ask_user_difficulty(self) -> str:
        user_select_difficulty = input("Select game difficulty level (0 for easy, 1 for medium, 2 for hard): ")
        return user_select_difficulty
