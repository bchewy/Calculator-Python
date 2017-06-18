# Ask for first number to be used
# Store first number
# Print statement to show numbers for different operators
# Ask for arithmetic operation to be used (+, - ,/ ,* ,**)
# Ask for second number to be used
# Store 2nd number
# Use 2nd number on first number with chosen arithmetic operation
# Tada!

##Declare 1st number for calculator
## store as float
no1 = float(input("Number one:"))
## create list with different operators
lst = ['+','-','/','*','**']
## print text for humans to understand which operator/how to choose operators
print("0 = +, 1 = - , 2 = / , 3 = * , 4= **")
## declare operator being chosen in lst variable(list)
op = lst[int(input("Operator:"))]
##declare 2nd number to be used on 1st number for calculator
no2 = float(input("Number two:"))
if op=="+":
    print("Result:",no1 + no2)
elif op=="-":
    print("Result:",no1 - no2)
elif op=="/":
    print("Result:",no1 / no2)
elif op=="*":
    print("Result:",no1 * no2)
elif op=="**":
    print("Result:",no1 ** no2)

# For this program, you're using the index of a list to select the operator!
# Another cool way to make a calculator program!
