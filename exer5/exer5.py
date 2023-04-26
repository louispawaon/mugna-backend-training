"""
Exer 5

Let the user insert 3 string, save it in a text file,
and display all the contents of the text file,
sorted alphabetically

"""

text_1 = input("Enter String 1: ")
text_2 = input("Enter String 2: ")
text_3 = input("Enter String 3: ")
words = [text_1,text_2,text_3]
words.sort()

try:
    with open("exer5/exer5.txt", "at") as f:
        for word in words:
            f.write(word+"\n")
except IOError as e:
    print(e)

try:
    with open("exer5/exer5.txt", "rt") as f:
        contents = sorted(f.readlines())
        contents = ''.join(contents)
        print(contents)
except IOError as e:
    print(e)
finally:
    f.close()