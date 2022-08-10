num1 = float(input('Enter 1st number: '))
op = input('Enter operation between numbers: ')
num2 = float(input('Enter 2nd number: '))

if op == "+":
    result = num1 + num2
    print(result)
elif op == "-":
    result = num1 - num2
    print(result)
elif op == "*":
    result = num1 * num2
    print(result)
elif op == "/":
    result = num1 / num2
    print(result)
else:
    print('Invalid operator')
