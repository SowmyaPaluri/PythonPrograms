def operate_numbers(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '//':
        return a // b
    elif op == '%':
        return a % b
    elif op == '**':
        return a ** b
    
print(operate_numbers(5,3,'+'))
print(operate_numbers(10,2,'-'))

    