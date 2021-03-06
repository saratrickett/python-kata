# DATA TYPES
#typing.io - typing practice for programmers
# str - string
_str = 'test'
_str2 = "tst"
_str3 = '{_str2} test'.format(_str2=_str2)
_str4 = f'{_str} test'

# bool - boolean
_bool = True
_bool_false = False

# int - integer
_int = 1
_int_negative = -1

# float
_float = 1.0
_float_negative = -1.0

# list
# dict

_list = ['alex', 'grande', 'sara',
         'danie', 'laura', 'jen']

for name in _list:
    print(name)

_list2 = list()

# casting

output = int('1') + 1
output2 = '1' + str(1)
print(output)
print(output2)

print(bool(0))
print(bool(1))
print(bool(.1))
print('---')

print(len(''))
print(len('false'))

print(bool('false'))
print(bool(None))
print(bool([]))

# for {variable_name} in <collection>:
# <action>
name = 'name'
for character in name:
    print(character)

"""
practice: create a function that takes an input, then prints each character of the input
"""

def print_character(input):
    for character in input:
        print(character)
print_character('supercalifragilistic')

"""practice: create a function that takes two inputs, then prints True/False whether or not
 the first input is contained within the second input """

# == compares
def search_character(search, find):
    for character in find:
        if character == search:
            print(True)
search_character('a','Sara')