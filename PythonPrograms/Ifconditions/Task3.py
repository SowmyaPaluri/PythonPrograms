# check vowel or not
l = input("Enter string: ")
if l in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Not a vowel")
    
    
    
# check capital or not
l = input("Enter string: ")
if l.isupper():
    print("Capital")
else:
    print("Not Capital")
    
    
    
# check small or not
l = input("Enter string: ")
if l.islower():
    print("Small")
else:
    print("Not Small")
    
    
# convert to opposite case
l = input("Enter string: ")
if l.isalpha():
    if l.isupper():
        print(l.lower())
    else:
        print(l.upper())
else:
    print("Error")
    