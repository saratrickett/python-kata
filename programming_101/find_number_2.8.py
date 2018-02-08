"""
    PRACTICE: create a function that takes two inputs,
    then prints True/False whether or not the first input
    is contained within the second input
"""
#def contain(first, second):
 #   for letter in second:
   #     if letter == first:
  #          print(True)
#contain('r', 'Sara')


""""""
text_value = 'some input'
def search_string(search, text_input):
    result = False 
    for character in text_input:
        if character == search:
            result = True
    print(result)


search_string('a', text_value) # False 
search_string('s', text_value) # True
search_string('S', text_value) # False
