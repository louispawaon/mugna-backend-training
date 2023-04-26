"""
Exer 3

Implement a simple FLAMES Games using Python!

Let the user input two names, in form of string, and compute 
for the output after a FLAMES game

"""

FLAMES_CHOICES=["FRIENDS","LOVERS","ACQUAINTANCES","MARRIAGE","ENEMIES","SIBLINGS"]

person_one = input("Enter Name 1: ").upper()
person_two = input("Enter Name 2: ").upper()

person_two_inp = person_two.replace(" ","")
person_one_inp = person_one.replace(" ","")

for char in person_one_inp:
    if char not in person_two_inp:
        person_one_inp = person_one_inp.replace(char, '')

for char in person_two_inp:
    if char not in person_one_inp:
        person_two_inp = person_two_inp.replace(char, '')        

count = len(person_one_inp)+len(person_two_inp)

#Person One
person_one_result=''
for i in range(len(person_one_inp)):
    index = i % len(FLAMES_CHOICES)  
    person_one_result=FLAMES_CHOICES[index]

#Person Two
person_two_result=''
for i in range(len(person_two_inp)):
    index = i % len(FLAMES_CHOICES)  
    person_two_result=FLAMES_CHOICES[index]

#Combined
combined_result=''
for i in range(count):
    index = i % len(FLAMES_CHOICES)  
    combined_result=FLAMES_CHOICES[index]

print(f"Result for {person_one} ==> {person_one_result}")
print(f"Result for {person_two} ==> {person_two_result}")
print(f"FINAL RESULT ==> {combined_result}")




