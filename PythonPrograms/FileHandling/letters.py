# read all letters into list and display
file = open("info.txt",'r')
#print(file.read(15))
print(file.read())
l = []
with open('info.txt','r') as file:
    for line in file:
        for i in line:
            l.append(i)
print(l)
