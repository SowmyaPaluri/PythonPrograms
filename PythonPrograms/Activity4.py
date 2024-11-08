# take 3 inputs print product if product is less than or equal to 1000 otherwise print their sum

a,b,c = map(int,input("Enter 3 numbers with spaces").split())
x = a * b * c
if x <= 1000:
    print(x)
else:
    print(a + b + c)