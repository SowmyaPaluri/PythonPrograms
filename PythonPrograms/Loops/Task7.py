# factorial of a number
n = int(input("Enter number: "))
fact, i = 1,1
while i <= n:
    fact *= i
    i += 1
print(fact)


# fibonocci series
n = int(input("Enter fibonocci number of terms"))
a,b = 0,1
i = 0
while i < n:
    c = a+b
    print(c,end=' ')
    a = b
    b = c
    i += 1
    
# Multiplication Table
n = int(input())
i = 1
while i <= 10:
    print(f"{n} * {i} = {n*i}")
    i += 1


