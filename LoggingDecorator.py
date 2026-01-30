#Create a decorator @log_execution_time that logs the time taken to execute a function. 
#Use it to log the runtime of a sample function calculate_sum(n) that returns the sum of numbers from 1 to n.

import time
from functools import wraps
def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result
    return wrapper
