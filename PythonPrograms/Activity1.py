# Prime numbers between 1 to 100 using for loop
for n in range(2,101):
    c = 0
    f = 0
    for i in range(1,n+1):
        if n % i == 0:
            c += 1
        if c > 2:
            f = 1
            break
    if f == 0:
        print(n,end=' ')
print()
        
        
# Prime numbers between 1 to 100 using while loop
n = 2
while n < 101:
    c = 0
    f = 0
    i = 1
    while i <= n:
        if n % i == 0:
            c += 1
        if c > 2:
            f = 1
            break
        i += 1
    if f == 0:
        print(n,end=' ')
    n += 1
print()



#check positive negative or zero

n = int(input("Enter any integer: "))
if n > 0:
    print("Positive")
elif n == 0:
    print("Zero")
else:
    print("Negative")
print()   
    
    
# count number of words in string
s = input("Enter any sentence: ")
print(len(s.split()))
print()



# first 10 even numbers
for i in range(2,21,2):
    print(i,end=' ')
print()


#swapping of 2 variables
a,b = 2,3

# method 1
# temp = a
# a = b
# b = temp

# method 2
# a = a + b
# b = a - b
# a = a - b

# method 3
# a = a ^ b
# b = a ^ b
# a = a ^ b

# method 4
a,b = b,a

print(a,b,end='\n')



# celsius to farenheit

c = int(input("Enter temperature in celsius: "))
print((c * (9/5)) + 32,end='\n')



# convert minuted to hours and minutes
n = int(input("Enter minutes: "))
hours = n // 60
min = n - (hours*60)
print(f"{hours}hrs {min}min",end='\n')



# Largest of 3 numbers

a,b,c = map(int,input("Enter 3 integers with spaces").split())
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)



