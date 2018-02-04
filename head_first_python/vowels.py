"""
PRACTICE: Determine if a given word contain any vowels and print those wowels only once.
"""

vowels = ['a', 'e', 'i', 'o', 'u']
word = "Millaways"
for letter in word:
    if letter in vowels:
        print (letter)