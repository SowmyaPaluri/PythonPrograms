for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
for i in range(1,6):
    for j in range(1,5-i+1):
        print(j,end=' ')
    print()




for i in range(1,6):
    for j in range(1,5-i+1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    print()
for i in range(1,6):
    for j in range(1,i+1):
        print(' ',end=' ')
    for k in range(1,5-i+1):
        print(k,end=' ')
    print()
print()




for i in range(1,6):
    for j in range(1,5-i+1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(1,end=' ')
    if i>1:
        for k in range(i,1,-1):
            print(1,end=' ')
    print()
for i in range(1,6):
    for j in range(1,i+1):
        print(' ',end=' ')
    for k in range(1,5-i+1):
        print(1,end=' ')
    for j in range(1,5-i):
        print(1,end=' ')
    print()
print()





for i in range(1,6):
    for j in range(1,5-i+1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    if i>1:
        for k in range(i,1,-1):
            print(k-1,end=' ')
    print()
for i in range(1,6):
    for j in range(1,i+1):
        print(' ',end=' ')
    for k in range(1,5-i+1):
        print(k,end=' ')
    for j in range(1,5-i):
        print(5-j-i,end=' ')
    print()
print()




