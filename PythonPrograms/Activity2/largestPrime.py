# write a function and return the largest prime number less than n
def largestprime(nn):
    for n in range(nn-1,2,-1):
        c = 0
        for i in range(1,n+1):
            if n % i == 0:
                c += 1
        if c == 2:
            return n

n = int(input("Enter any number: "))
print(largestprime(n))
