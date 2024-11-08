# create a list and take 1 input integers and find the biggest integer

l = []
max = float('-inf')
for i in range(1,11):
    x = int(input(f"Enter {i} interger: "))
    l.append(x)
    if max < x:
        max = x
print(max)


# create a list and take 1 input integers and find the second biggest integer

l = []
for i in range(1,11):
    x = int(input(f"Enter {i} interger: "))
    l.append(x)
if l[0] > l[1]:
    max1 = l[0]
    max2 = l[1]
else:
    max1 = l[1]
    max2 = l[0]
for i in range(2,10):
    if max1 < l[i]:
        max2 = max1
        max1 = l[i]
    elif max2 < l[i]:
        max2 = l[i]
print(max2)



# create a list and display them in ascending order

a = []
for i in range(1,11):
    x = int(input(f"Enter {i} interger: "))
    a.append(x)
for i in range(len(a)):
    for j in range(1,len(a)-i):
        if a[j-1] > a[j]:
            a[j-1],a[j] = a[j],a[j-1]
print(a)


# create a list and display them in descending order

a = []
for i in range(1,11):
    x = int(input(f"Enter {i} interger: "))
    a.append(x)
for i in range(len(a)):
    for j in range(1,len(a)-i):
        if a[j-1] < a[j]:
            a[j-1],a[j] = a[j],a[j-1]
print(a)


# create a list and search for an element in which position

a = []
for i in range(1,11):
    x = int(input(f"Enter {i} interger: "))
    a.append(x)
key = int(input("Enter element to be searched: "))
for i in range(len(a)):
    if a[i] == key:
        print(f"Found at index {i}")
        break
else:
    print("Not Found")