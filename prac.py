num1 = float(input('Enter num1: '))
num2 = float(input('Enter num2: '))
operator = input('Enter operator: ')

if operator == '+':
    print(f'{num1} {operator} {num2} = amount: {num1+num2: .2f}')
elif operator == '-':
    print(f'{num1} {operator} {num2} = amount: {num1-num2: .2f}')
elif operator == '*':
    print(f'{num1} {operator} {num2} = amount: {num1*num2: .2f}')
elif operator == '/':
    print(f'{num1} {operator} {num2} = amount: {num1/num2: .2f}')
else:
    print('Invalid Operator')