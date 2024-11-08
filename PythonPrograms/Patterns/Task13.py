for i in range(1,6):
    for j in range(1,6):
        print(1,end=' ')
    print()
print()



for i in range(1,6):
    for j in range(1,6):
        if i % 2 != 0:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
print()



for i in range(1,6):
    for j in range(1,6):
        if (i>=2 and i<=4) and (j>=2 and j<=4):
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()
print()



for i in range(1,6):
    for j in range(1,6):
        if (i>=2 and i<=4) and (j>=2 and j<=4):
            print(' ',end=' ')
        else:
            print(1,end=' ')
    print()
print()