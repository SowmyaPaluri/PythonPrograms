a = 25
b = 'a'
try:
    result = a/b
except ZeroDivisionError:
    print("Error: You cannot divide a number by zero")
    result = None
except TypeError:
    print("Error: Both arguments must be of same type")
    result = None
else:
    print(result)
finally:
    print("Exception is handled successfully")
    