def leapyear(n):
    if n % 100 and n % 400 == 0:
        return True
    elif n % 100 != 0 and n % 4 == 0:
        return True
    return False

year = int(input("Enter year: "))
print(leapyear(year))