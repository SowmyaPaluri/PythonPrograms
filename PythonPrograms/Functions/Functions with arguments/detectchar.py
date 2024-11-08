# detect character small,capital,digit,space or special letter

def detectchar(c):
    if c >= 'A' and c <= 'Z':
        print("Capital")
    elif c >= 'a' and c <= 'z':
        print("Small")
    elif c >= '0' and c <= '9':
        print("Digit")
    elif c == ' ':
        print("Space")
    else:
        print("Special letter")

c = input("Enter any character: ")
detectchar(c)