def sumOfDigits(n):
    s = 0
    while n > 0:
        d = n % 10
        s += d
        n = n // 10
    return s


n = int(input("Enter number: "))
print(sumOfDigits(n))