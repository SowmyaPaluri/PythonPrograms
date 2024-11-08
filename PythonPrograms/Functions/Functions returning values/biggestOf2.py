# biggest of 2 numbers

def biggest(a,b):
    if a>b:
        return a
    else:
        return b
    
a,b = map(int,input("Enter 2 unique interges with space separated: "))
print(biggest(a,b))