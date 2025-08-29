# Write a program to demonstrate multithreading by
#  creating and running multiple threads to perform different tasks
#  simultaneously.


import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Both threads have finished")