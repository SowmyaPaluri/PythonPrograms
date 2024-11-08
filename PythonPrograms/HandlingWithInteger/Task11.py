# count of factors
# sum of factors
# prime or not
# perfect or not

n = int(input("Enter any number"))
c,f,s = 0,0,0
for i in range(1,n+1):
    if n % i == 0:
        c += 1
        s += i
print(c,s)
print("Prime" if c == 2 else "Not Prime")
print("Perfect" if s-n == n else "Not Perfect")