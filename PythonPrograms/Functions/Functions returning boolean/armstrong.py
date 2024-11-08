def armstrong(n):
    x,asum = n,0
    while n > 0:
        d = n % 10
        asum += d**(len(str(x)))
        n = n // 10
    return x == asum

n = int(input("Enter number: "))
print(armstrong(n))

