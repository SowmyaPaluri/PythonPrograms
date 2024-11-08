def palindrome(n):
    rev,x = 0,n
    while n > 0:
        d = n % 10
        rev = rev*10+d
        n = n // 10
    return x == rev

n = int(input("Enter number: "))
print(palindrome(n))
