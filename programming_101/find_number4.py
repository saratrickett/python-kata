"""
  PRACTICE: print each letter in a given string
"""
string = 'eagles'

for letter in string:
    print(letter)

"""
  PRACTICE: create a function that takes an input,
  then prints each character of the input
"""

def print_character(input):
    for character in input:
        print(character)
print_character('coding')
print_character('oranges')
"""
    PRACTICE: create a function that takes two inputs,
    then prints True/False whether or not the first input
    is contained within the second input
"""

def contain(first, second):
    for character in first:
        if character in second:
            print(True)
        else:
            print(False)
contain('b', 'boy')