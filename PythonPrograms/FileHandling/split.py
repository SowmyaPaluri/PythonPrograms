file = open("text.txt",'r')
with open('text.txt','r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
        
        
