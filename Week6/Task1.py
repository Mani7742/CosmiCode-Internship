#  Write a program to demonstrate the use of decorators to measure the execution time of functions.

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of '{func.__name__}': {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def sample_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

@timing_decorator
def sleep_function():
    time.sleep(2)

if __name__ == "__main__":
    print("Starting program...")
    sample_function()
    sleep_function()
    print("Program finished.")