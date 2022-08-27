from fizzbuzz import fizzbuzz


def test_fizzbuzz():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz('7') == 7
    assert fizzbuzz('3') == 'Fizz'
    assert fizzbuzz('-5') == 'Buzz'
    assert fizzbuzz('hhh') is None
    assert fizzbuzz(7) == 7
