# DATA TYPES
# str - string
# bool - boolean
# int - integer
# float
# list

# CASTING
# str + int = runtime exception


# CONTROL STRUCTURES
# --for loops--
# for {variable_name} in <collection>:
#     <action>
#
# --logical--
# if <bool>:
#   pass
# elif <bool>:
#   pass
# else <bool>:
#   pass
#
# --comparisons--
# == -> equals
# != -> not equals
# > -> greater than
# >= -> greater than equal
# < -> less than
# <= -> les than equal

count = 1
    if count == 2:
        print ('1')
        print('Done')



"""
  PRACTICE: print each letter in a given string
"""
text_value = 'some input'

print('\n'.join(text_value))


string = "pineapple"

for letter in string:
    print(letter)
"""
  PRACTICE: create a function that takes an input,
  then prints each character of the input
"""
def print_character(input):
    for letter in input:
        print(letter)
print_character('Sara')
"""
    PRACTICE: create a function that takes two inputs,
    then prints True/False whether or not the first input
    is contained within the second input
"""
def contain(first, second):
    for letter in second:
        if letter == first:
            print(True)
contain('r', 'Sara')
