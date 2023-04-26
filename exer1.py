"""
Exer1

Instruction

Write a program that accepts an input value (range: 60-100)
and prints a message based on the following range of values:

RANGE                   MESSAGE
60-74                   Derp!
75-84                   Good
85-94                   Very Good
95-100                  Excellent!
any other value         Invalid Value

"""

value = int(input("Enter a value: "))

if value >= 60 and value <= 74:
    print("Derp!")
elif value >= 75 and value <= 84:
    print("Good")
elif value >= 85 and value <= 94:
    print("Very Good")
elif value >= 95 and value <= 100:
    print("Excellent!")
else:
    print("Invalid Value")