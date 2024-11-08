def perfectNumber(n):
    s = 0
    for i in range(1,n+1):
        if n % i == 0:
            s += i
    return s-n == n


n = int(input("Enter any number: "))
print(perfectNumber(n))
