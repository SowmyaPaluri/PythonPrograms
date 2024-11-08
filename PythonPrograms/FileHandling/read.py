file = open("info.txt",'r')
#print(file.read(15))
print(file.read())

with open('info.txt','r') as file:
    for line in file:
        print(line,end='')
        
