f1 = open("pic.txt",'rb')
f2 = open("newpic.txt",'wb')
bytes = f1.read()
f2.write(bytes)
print("New image is available with the name: newpic.jpg")


