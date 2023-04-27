import math
import datetime
from math import sqrt
from os import *

def take_all_list(arg1, arg2, arg3=0, *args, **kwargs):
    """
    Docstring for take_all_list. Basically, this is a useless function, but would test how well you know about PEP-8.
    """
    list_a = [1, 2, 3, 4, 5]
    var_b = list_a[0] * list_a[1] + list_a[2] - (3 + list_a[3])
    print(arg1, arg2)
    if arg3 != 0:
        print(arg3)
    if 5 < arg3 < 10:
        list_a.append(arg3)
        print(f"This is to ensure that our list would be printed ==> {list_a}")
    else:
        list_a = None
    print(var_b)
    if list_a is not None:
        print("list_a has an entry")

def print_all_number(n):
    m = 0
    first = n
    second = n + 1
    third = n + 2
    fourth = n + 3
    print(first, second, third, fourth)
    for n in range(n):
        print(n)
        m += n 
        print(m)  
    checker = m > sum(range(n))
    if checker:
        print("TAMA!")
    else:
        print("MALI!")

class ThisIsStudentClass:
    FIRSTNAME = 'A'
    LASTNAME = 'A'

    def __init__(self, age, address):
        self.AGE = age
        self.ADDRESS = address

    def get_name(self):
        return f"{self.LASTNAME}, {self.FIRSTNAME}"

def another_function():
    print(math.pi)
    sqrt_of_pi = sqrt(math.pi)
    print("It's the square root of pi", sqrt_of_pi)
    string_sample = "Why, hello there!"
    print(string_sample[1::2])
    take_all_list(1, 2, 3)
    try:
        l = 2
        m = 3
        n = l + m
    except Exception:
        print("ERROR!")
        return math.pi
    take_all_list(l, m, n)



"""
Changes

- Removed Comments
- Spaces after commas in function arguments
- Used snake_case for function and variable names
- Added spaces for binary operators
- Added spaces after comment symbol ("#")
- Used "is not None" instead of "!=None"
- Used f string instead of str.format()
- Used blank lines after a function definition
- Used PascalCase for class names and camelCase for method names 
- Added self parameter in class methods
- Added try-except block with Exception

"""