"""
PRACTICE: Determine if a given word contain any vowels and print those wowels only once.
"""

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels:")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)