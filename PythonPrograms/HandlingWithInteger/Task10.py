# sum of the digits
# number of digits
# even number of digits
# sum of even digits
# reverse of a number
# palindrome or not
# armstrong or not

n = int(input("Enter number: "))
sod,nod,ed,soed,rev,x,asum = 0,0,0,0,0,n,0
while n > 0:
    d = n % 10
    nod += 1
    if d % 2 == 0:
        ed += 1
        soed += d
    sod += d
    rev = rev*10+d
    asum += d**(len(str(x)))
    n = n // 10
print(sod,nod,ed,soed,rev)
print("Palindrome" if x == rev else "Not Palindrome")
print("Armstrong" if x == asum else "Not Armstrong")

