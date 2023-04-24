'''
Exer 4

Write a program wich counts the occurences of words of words from
a given string and stores the words and corresponding counts as key-value
pairs in a dictionary

'''

given_text = input("Enter string: ").lower()
clean_text = ''.join(char for char in given_text if char.isalnum() or char.isspace())
occurence = {word: clean_text.split().count(word) for word in clean_text.split()}
print(occurence)
