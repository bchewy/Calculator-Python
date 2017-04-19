# Ask for first number to be used
# Store first number
# Print statement to show numbers for different operators
# Ask for arithmetic operation to be used (+, - ,/ ,* ,**)
# Ask for second number to be used
# Store 2nd number
# Use 2nd number on first number with chosen arithmetic operation
# Tada!

no1 = float(input("Number one:"))
lst = ['Addition','Subtraction','Division','Multiplication']
print("0 = +, 1 = - , 2 = / , 3 = *")
op = lst[int(input("Operator:"))]
no2 = float(input("Number two:"))
if op=="Addition":
    print("Result:",no1 + no2)
elif op=="Subtraction":
    print("Result:",no1 - no2)
elif op=="Division":
    print("Result:",no1 / no2)
elif op=="Multiplication":
    print("Result:",no1 * no2)

