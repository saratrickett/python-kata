"""
You can't write any production code until you have first written a failing unit test.
You can't write more of a unit test than is sufficient to fail, and not compiling is failing.
You can't write more production code than is sufficient to pass the currently failing unit test.

red-green-refactor

fake it til you make it

YAGNI
you ain't going to need it

ZOMBIES
zero
one
many
boundaries
interfaces
exceptions
simplicity
"""
from programming_101.fizz_buzz.fizz_buzz import fizz_buzz

def test_fizz_buzz_zero ():
    expected_result = ['1']
    result = fizz_buzz(1)
    assert expected_result == result

def test_fizz_buzz_one():
    expected_result = ['1', '2']
    result = fizz_buzz(2)
    assert expected_result == result

def test_fizz_buzz_fizz():
    expected_result = ['1', '2', 'fizz']
    result = fizz_buzz(3)
    assert expected_result == result

def test_fizz_buzz_buzz():
    expected_result = ['1', '2', 'fizz', '4', 'buzz']
    result = fizz_buzz(5)
    assert expected_result == result

# def test_fizz_buzz_fizzbuzz():
#     expected_result = ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
#     result = fizz_buzz(15)
#     assert expected_result == result