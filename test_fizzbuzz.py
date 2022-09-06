from fizzbuzz import *

def test_str2num():
    assert str2num('  7   ') == 7
    assert str2num('5.8') == 6
    assert str2num('  5.8   ', 1) == 5.8
    assert str2num('  -14   ', 1) == -14.0
    assert str2num('ggg') != str2num('ggg')


def test_fizzbuzz():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(7) == '7'
