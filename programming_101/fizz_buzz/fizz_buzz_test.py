"""
You can't write any production code until you have first written a failing unit test.
You can't write more of a unit test than is sufficient to fail, and not compiling is failing.
You can't write more production code than is sufficient to pass the currently failing unit test.

red-green-refactor

fake it til you make it

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
    expected_result = ['0']
    result = fizz_buzz(0)
    assert expected_result == result