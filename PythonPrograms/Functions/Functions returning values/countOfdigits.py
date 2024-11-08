# number of digits

def countOfDigits(n):
    nod = 0
    while n > 0:
        d = n % 10
        nod += 1
        n = n // 10
    return nod


n = int(input("Enter number: "))
print(countOfDigits(n))