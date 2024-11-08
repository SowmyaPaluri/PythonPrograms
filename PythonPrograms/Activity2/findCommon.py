# finding common elements from 2 lists

def findCommon(l1,l2):
    return list(set(l1)&set(l2))

l1 = [1,2,3,4]
l2 = [3,4,5,6]
print(findCommon(l1,l2))