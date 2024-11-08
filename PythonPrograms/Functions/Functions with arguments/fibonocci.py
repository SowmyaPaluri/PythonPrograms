# fibonocci series

def fib(n):
    a,b = 0,1
    i = 0
    while i < n:
        c = a+b
        print(c,end=' ')
        a = b
        b = c
        i += 1
        
n = int(input("Enter fibonocci number of terms"))
print(fib(n))
