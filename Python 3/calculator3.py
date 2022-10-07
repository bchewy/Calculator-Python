# CODE IS FROM https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3
# LICENSED Attribution-NonCommercial-ShareAlike
# 4.0 International (CC BY NC-SA 4.0)
# CODE IS NOT OWNED BY ME
# Improved certain sections and added various other functions
import math
def mode():
    mode = True
    while mode == True:
        try:
            return {"1":1,"2":2}[input('''
==========================
MODE 1 - Default Calculator                 |
MODE 2 - Conversion                          |
===========================
Type 1 or 2 ONLY
Mode Number : ''')]
        except (ValueError,TypeError,KeyError):
            print("Please select only 1 or 2.")

        
mode()

def calculator():

    number_1 = float(input('Please enter the first number: '))
    operation = input('''
Please type in the math operation you would like to complete:
===========================
+ for addition
- for subtraction
* for multiplication
/ for division
^ for power
sqrt for squareroot
degtorad for Degree to Radian Conversion
radtodeg for Radian to Degree Conversion
pi/ - Number 1 / pi
pi* - Number 1 * pi
fact - Factorial of a no1
===========================
Enter operator: ''')
    if operation =='degtorad':
        print('{} deg converted to ='.format(number_1),end='')
        print(math.radians(number_1),'radians')
    elif operation =='fact':
        print("{}'s factorial is {}".format(number_1,math.factorial(number_1)))

    elif operation =='radtodeg':
        print('{} rad converted to ='.format(number_1),end='')
        print(math.degrees(number_1),'degrees')
    elif operation =='sqrt':
        print('{} square root = '.format(number_1), end='')
        print(math.sqrt(number_1))
    elif operation == 'pi/':
        print('{} / pi = '.format(number_1), end='')
        print(number_1 / math.pi)
    elif operation == 'pi*':
        print('{} * pi = '.format(number_1), end='')
        print(number_1 * math.pi)
    elif operation != 'sqrt' or 'degtorad' or 'radtodeg' or 'pi/' or 'pi*':
        number_2 = int(input('Please enter the second number: '))
        if operation == '+':
            print('{} + {} = '.format(number_1, number_2), end='')
            print(number_1 + number_2)
        elif operation == '-':
            print('{} - {} = '.format(number_1, number_2), end='')
            print(number_1 - number_2)
        elif operation == '*':
            print('{} * {} = '.format(number_1, number_2), end='')
            print(number_1 * number_2)
        elif operation == '/':
            print('{} / {} = '.format(number_1, number_2), end='')
            print(number_1 / number_2)
        elif operation == '^':
            print('{} ^ {} = '.format(number_1, number_2), end='')
            print(number_1 ** number_2)

    else:
        print('You are not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
ENTER HERE:  ''')

    if calc_again.upper() == 'Y':
        calculator()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculator()
