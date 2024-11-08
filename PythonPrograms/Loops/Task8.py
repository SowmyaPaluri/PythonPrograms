a,b = map(int,input("Enter 2 numbers: ").split())
print("Menu:\n1. Add\n2. Sub\n3. Mul\n4. Div\n5. Exit\n")
while True:
    n = int(input("Enter Choice: "))
    if n == 1:
        print(a+b)
    elif n == 2:
        print(a-b)
    elif n == 3:
        print(a*b)
    elif n == 4:
        print(a/b)
    elif n == 5:
        print("Exit")
        break