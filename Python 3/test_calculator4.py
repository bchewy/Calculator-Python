# content of test_sample.py


def add(*args):
    if(len(args) > 10):
        print("error > 10 values given")
        return "Error: >10 Values"

    result = args[0]
    for i in range(1, len(args)):
        result = result + args[i]

    print("Result is", result)
    return result


def subtract(*args):
    if(len(args) > 10):
        print("error > 10 values given")
        return "Error: >10 Values"

    result = args[0]
    for i in range(1, len(args)):
        result = result - args[i]

    print("Result is", result)
    return result


def multiply(*args):
    if(len(args) > 10):
        print("error > 10 values given")
        return "Error: >10 Values"

    result = args[0]
    for i in range(1, len(args)):
        result = result * args[i]

    print("Result is", result)
    return result


def divide(*args):
    if(len(args) > 10):
        print("error > 10 values given")
        return "Error: >10 Values"

    result = args[0]
    try:
        for i in range(1, len(args)):
            result = result / args[i]

        print("Result is", result)
        return result
    except ZeroDivisionError:
        print("Division by zero error at number", i+1)
        return ZeroDivisionError


print(divide(10, 2))
print(multiply(10, 2))
print(add(10, 2))
print(subtract(10, 2))


# Addition tests
def test_add_positive():
    assert add(1, 2, 3, 4) == 10


def test_add_negative():
    assert add(1, 2, 3, 5) != 10


def test_add_length_positive():
    assert add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 55


def test_add_length_negative():
    assert add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) == "Error: >10 Values"


# Subtraction tests

def test_subtract_positive():
    assert subtract(1, 2, 3, 4) == -8


def test_subtract_negative():
    assert subtract(1, 2, 3, 5) != -10


def test_subtract_length_positive():
    assert subtract(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == -53


def test_subtract_length_negative():
    assert subtract(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) == "Error: >10 Values"
# Multiplication tests


def test_multiply_positive():
    assert multiply(5, 2) == 10


def test_multiply_negative():
    assert multiply(1, 2, 3, 5) != 24


def test_multiply_length_positive():
    assert multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 3628800


def test_multiply_length_negative():
    assert multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) == "Error: >10 Values"


def test_multiply_zero():
    assert multiply(10, 0) == 0

# Division tests


def test_division_positive():
    assert divide(10, 2) == 5


def test_division_negative():
    assert divide(10, 3) != 5


def test_division_length_positive():
    assert divide(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 2.7557319223985894e-07


def test_division_length_negative():
    assert divide(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) == "Error: >10 Values"


def test_divide_zero():
    assert divide(10, 0) == ZeroDivisionError
