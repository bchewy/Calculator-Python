no1 = float(input("Number one:"))
lst = ['+','-','/','*','**','%']
print("0 = +, 1 = - , 2 = / , 3 = * , 4= **,5=%")
op = lst[int(input("Operator:"))]
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
elif op=="%":
    print("Result:",no1 % no2)
