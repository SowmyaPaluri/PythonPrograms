l = ['apple','banana','mango','orange']
print("Menu:\n1.List of Fruits\n2.Add a fruit\n3.Search for a fruit\n4.Delete a fruit\n5.Edit a fruit\n6.Exit")
while True:
    n = int(input("Enter your choice: "))
    if n == 1:
        print(l)
    elif n == 2:
        x = input("Enter a fruit to add into the fruits list: ")
        l.append(x)
    elif n == 3:
        x = input("Enter a fruit to be searched in the fruits list: ")
        print("fruit is there" if x in l else "fruit is not there")
    elif n==4:
        x = input("Enter a fruit to delete from the fruits list: ")
        l.remove(x)
    elif n == 5:
        x = input("Enter a fruit to edit from the fruits list: ")
        xi = l.index(x)
        y = input("Enter new fruit to add into the fruits list: ")
        l[xi] = y 
    else:
        print("Exit")
        break
        
