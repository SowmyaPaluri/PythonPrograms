# count of all letters, capital letters, small letters and zero letters in the file
file = open("info.txt",'r')
#print(file.read(15))
print(file.read())
u,l,z,c = 0,0,0,0
with open('info.txt','r') as file:
    for line in file:
        for i in line:
            if i.isupper():
                u += 1
            elif i.islower():
                l += 1
            elif i == ' ':
                z += 1
            c += 1
print(f"count of all letters is {c}")
print(f"count of capital letters is {u}")
print(f"count of small letters is {l}")
print(f"count of zero letters is {z}")

