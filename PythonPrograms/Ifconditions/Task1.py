# check positive negative or zero

n = int(input("Enter any integer: "))
if n > 0:
    print("Positive")
elif n == 0:
    print("Zero")
else:
    print("Negative")




# check even or odd

n = int(input("Enter any integer: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")




# check marks valid or invalid

n = int(input("Enter marks: "))
if n >= 0 and n <= 100:
    print("Valid")
else:
    print("Invalid")




# Largest of 3 numbers

a,b,c = map(int,input().split())
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

