def reverseOfInteger(n):
    rev = 0
    while n > 0:
        d = n % 10
        rev = rev*10+d
        n = n // 10
    return rev


n = int(input("Enter number: "))
print(reverseOfInteger(n))