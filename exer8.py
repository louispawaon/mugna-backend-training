'''
Exer 8

Create a decorator that would compute and display the 
time it took to run the function, in milliseconds 
(round off to 2 decimal places)

'''
import time

def timing_decorator(param):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = param(*args,**kwargs)
        end_time = time.time()
        elapsed_time = (end_time-start_time)*1000
        print(f"The time it took to run the function: {elapsed_time:.2f} ms")
        print(f"The sum is {res}.")
        return res
    return wrapper

@timing_decorator
def adding_function(x,y):
    return x+y

adding_function(3,5)