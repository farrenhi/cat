from typing import List

def print_history(user_attempts: List[int] = [], feedbacks: List[str] = []) -> None:
    if not len(user_attempts):
        print("No history data...")
    
    for i, (attempt, feedback) in enumerate(zip(user_attempts, feedbacks), start=1):
        print(f"User Attempt {i}: {attempt}, Feedback: {feedback}")

def present_to_user(statement: str = None) -> None:
    if statement:
        print(statement)

def ask_user_guess() -> str:
    user_input = input("Guess a sequence of four numbers (ex: 3102) or enter h for history: ")
    return user_input