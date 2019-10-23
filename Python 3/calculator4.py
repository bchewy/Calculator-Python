# Re-written python code for school
# a.	Addition of multiple numbers depending on user needs, up to a maximum of 10 additions.
# b.	Subtraction of multiple numbers depending on user needs, up to a maximum of 10 subtractions.
# c.	Multiplication of multiple numbers depending on user needs, up to a maximum of 10 multiplications.
# d.	Division of multiple numbers depending on user needs, up to a maximum of 10 divisions


def add(*args):
    return sum(args[0])


def subtract(*args):
    total = 0
    for i in args:
        for x in i:
            print(x)
            total = total - x
            print(total)
    return total


print(subtract([1, 2, 3, 4]))


def multiply(*args):
    total = 0
    for i in args:
        for x in i:
            total *= x
    return total


def divide(*args):
    total = 0
    for i in args:
        for x in i:
            total /= x
    return total


def request_input():
    x = 0
    arrayNumbers = []
    while x < 10:
        try:
            value = str(
                input('Please enter the number, or the letter S to stop:'))
            if value.upper() == 'S':
                break
            arrayNumbers.append(int(value))
            x += 1
        except (ValueError):
            print('Sorry, Please key in a valid value!')
    print(arrayNumbers)
    return arrayNumbers

# print(add(request_input()))
# print(subtract(request_input()))
# print(multiply(request_input()))
# print(divide(request_input()))
