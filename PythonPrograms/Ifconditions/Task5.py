pmr,lmr = map(int,input().split())
bu = pmr - lmr
if bu < 200:
    ur = 1.5
elif bu < 400:
    ur = 2.75
elif bu < 500:
    ur = 3.45
else:
    ur = 7
print(bu*ur)