import threading
import time
import sys
import controller

import view_command_line
import model


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

def input_numbers(view):
    controller.play(view)


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
    input_thread = threading.Thread(target=input_numbers, args=(view, ), daemon=True)
    
    # If daemon is set to True, it means the thread will run as a daemon thread. 
    # Daemon threads are background threads that 
    # do not prevent the program from exiting if they are still running when the main thread finishes.

    input_thread.start()
    countdown_thread.start()
    
    # countdown_thread.join()
    # input_thread.join()
    sys.exit()

    
