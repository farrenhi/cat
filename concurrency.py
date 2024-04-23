import threading
import time
import sys
import controller
import shared_variables
import view_command_line
import model

def countdown_timer(duration, timer_completed):
    # global remaining_time
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        # remaining_time = int(end_time - time.time())
        time_updated = int(end_time - time.time())
        shared_variables.remaining_time['time'] = time_updated
        
        if shared_variables.input_thread['end']:
            sys.exit()
        
        # Print timer on the same line
        # print(f"\rTime remaining: {remaining_time} seconds. Enter a number:", end="")  
        # sys.stdout.flush()
        
        # The \r character is a carriage return, which moves the cursor to the beginning of the line 
        # without advancing to the next line, effectively allowing the new message 
        # to overwrite the previous one.
        # print(remaining_time['time'])
        time.sleep(1)

    print(f"\nTime's up! Game ended. The secret code is: {shared_variables.secret_code}")
    attempts_left = shared_variables.input_thread['attempts_left']
    score = model.calculate_score(shared_variables.difficulty_config[shared_variables.difficulty_level[0]],
                            attempts_left, shared_variables.remaining_time['time'], False,
                            shared_variables.counter_correct_numbers,
                            shared_variables.counter_position_booleans
                            )
    view_command_line.present_to_user(f"Your score: {score}")
    timer_completed.set()  # Set the flag to indicate that the timer has completed
    # sys.exit()

# def input_numbers(timer_completed):
#     # global remaining_time
    
#     while True:  # Continuously ask for input until the timer expires
#         user_input = input("\nEnter a number: ")
#         if timer_completed.is_set():  # Check if the timer has expired
#             break
#         print("user_input:", user_input)
#         print("remaining time:", remaining_time['time'], "second(s)")
#         # task: i would like to print remaining time here. how should i do that?
#     # sys.exit()

def input_numbers():
    controller.play()


# def input_numbers(timer_completed):
#     while not timer_completed.is_set():  # Continue asking for input while the timer hasn't expired
#         if timer_completed.is_set():  # Check if the timer has expired
#             break
#         user_input = input("Enter a number: ")
#         print("user_input:", user_input)


if __name__ == "__main__":
    timer_completed = threading.Event()

    countdown_thread = threading.Thread(target=countdown_timer, args=(60, timer_completed))
    # , daemon=True
    
    # input_thread = threading.Thread(target=input_numbers, args=(timer_completed, ), daemon=True)
    input_thread = threading.Thread(target=input_numbers, daemon=True)
    
    # If daemon is set to True, it means the thread will run as a daemon thread. 
    # Daemon threads are background threads that 
    # do not prevent the program from exiting if they are still running when the main thread finishes.

    input_thread.start()
    countdown_thread.start()
    
    # countdown_thread.join()
    # input_thread.join()
    sys.exit()

    
