# TABLE

def table(n):
    i = 1
    while i <= 10:
        print(f"{n} * {i} = {n*i}")
        i += 1
        
n = int(input("Enter number: "))
table(n)