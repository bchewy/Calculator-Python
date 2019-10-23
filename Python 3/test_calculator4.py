# content of test_sample.py
def add(*args):
    return sum(args[0])


def subtract(*args):
    total = 0
    for i in args:
        for x in i:
            total -= x
    return total


# Cannot take in any zero values or the resulting total will be zero.
def multiply(*args):
    total = 1
    for i in args:
        for x in i:
            print(x)
            total = (total * x)
            print(total)
    return total

# Cannot take in any zero values or the resulting total will be zero.


def divide(*args):
    for i in args:
        for x in i:  # i being the array
            total = x
    return total


print(divide([10, 2]))


def test_add_positive():
    assert add([1, 2, 3, 4]) == 10


def test_add_negative():
    assert add([1, 2, 3, 5]) != 10


def test_subtract_positive():
    assert subtract([1, 2, 3, 4]) == -10


def test_subtract_negative():
    assert subtract([1, 2, 3, 5]) != -10


def test_multiply_positive():
    assert multiply([5, 2]) == 10


def test_multiply_negative():
    assert multiply([1, 2, 3, 5]) != 24


def test_division_positive():
    assert divide([10, 2]) == 5


def test_division_negative():
    assert divide([10, 3]) != 5
