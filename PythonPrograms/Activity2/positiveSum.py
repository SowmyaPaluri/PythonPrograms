# Find sum of all positive integers from the given list

def positiveSum(l):
    s = 0
    for i in l:
        if i > 0:
            s += i
    return s

l = [1,500,-5,6,-7,9,-100]
print(positiveSum(l))