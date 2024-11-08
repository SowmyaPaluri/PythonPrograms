# from num2words import num2words
# n = int(input())
# print(num2words(n))

n = int(input())
d = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
dd = {11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
tens ={1:'ten',2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
os = n % 10
ts = (n//10) % 10
res = ''
if ts > 1 and os != 0:
    res += tens[ts]
    res += ' '
    res += d[os]
elif os == 0:
    res += tens[ts]
else:
    res += dd[n]
print(res+' only')