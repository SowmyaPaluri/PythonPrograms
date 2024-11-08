def countOfEvenDigits(n):
    nod = 0
    while n > 0:
        d = n % 10
        if d % 2 == 0:
            nod += 1
        n = n // 10
    return nod


n = int(input("Enter number: "))
print(countOfEvenDigits(n))