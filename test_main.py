from main import fizbuz

def test_fizbuz():
    assert fizbuz(3) == 'Fizz'
    assert fizbuz(5) == 'Buzz'
    assert fizbuz(15) == 'FizzBuzz'
    assert fizbuz(7) == 7
