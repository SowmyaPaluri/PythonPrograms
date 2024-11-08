# 1. abs()

# Purpose: Returns the absolute (non-negative) value of a number.
# Syntax: abs(x)
# Useful for ensuring positive values in cases like distance or magnitude calculations.
# Example:
print(abs(-7))   # Output: 7
print(abs(3.5))  # Output: 3.5



# 2. aiter()

# Purpose: Returns an asynchronous iterator for asynchronous iterables, introduced in Python 3.10.
# Syntax: aiter(async_iterable)
# Used in asynchronous programming with async for to iterate over asynchronous data sources.
# Example:
import asyncio
async def example():
    async for value in aiter(async_iterable):
        print(value)



#3. all()

# Purpose: Returns True if all elements in an iterable (e.g., list, tuple) are True (or if the iterable is empty).
# Syntax: all(iterable)
# Useful in situations where you need to check if all conditions in a collection are met.
# Example:
print(all([True, True, 1, "hello"]))  # Output: True
print(all([True, False, 1]))         # Output: False



# 4. any()

# Purpose: Returns True if at least one element in an iterable is True.
# Syntax: any(iterable)
# Helpful for checking if any conditions in a collection are met.
# Example:
print(any([False, False, True]))  # Output: True
print(any([False, False]))        # Output: False





# 5. anext()

# Purpose: Retrieves the next item from an asynchronous iterator, introduced in Python 3.10.
# Syntax: await anext(async_iterator[, default])
# Often used with asynchronous loops where asynchronous data is processed step-by-step.
# Example:
async def example():
    try:
        value = await anext(async_iterator)
        print(value)
    except StopAsyncIteration:
        pass
    
    
    
# 6. ascii()
# Purpose: Returns a string representation of an object, escaping non-ASCII characters.
# Syntax: ascii(object)
# Useful for ensuring output is in ASCII, especially when working with files or data exchange where ASCII compatibility is required.
# Example:
print(ascii("Hello, Мир!"))  # Output: 'Hello, \u041c\u0438\u0440!'



# 1. bin()

# Purpose: Converts an integer to its binary representation as a string prefixed with "0b".
# Syntax: bin(x)
# Use Case: Useful for visualizing binary data, such as bitwise operations or when working with binary-based calculations.
# Example:
print(bin(10))  # Output: '0b1010'



# 2. bool()

# Purpose: Converts a value to a Boolean (True or False). It returns False for values like 0, None, '', [], and True for most other values.
# Syntax: bool(x)
# Use Case: Commonly used to test the truthiness of a value or condition in conditional statements.
# Example:
print(bool(0))         # Output: False
print(bool("Hello"))   # Output: True



# 3. breakpoint()

# Purpose: Enters the Python debugger at the point where it is called, allowing you to inspect the current state of the program.
# Syntax: breakpoint()
# Use Case: Ideal for debugging, as it opens an interactive debugging session to inspect variables, run commands, and step through code.
# Example:
x = 10
breakpoint()  # Program pauses here for debugging
y = x * 2



# 4. bytearray()

# Purpose: Returns a mutable sequence of bytes, which can be modified after creation.
# Syntax: bytearray([source, encoding, errors])
# Use Case: Useful when working with binary data that requires modification, such as handling image or audio files in byte format.
# Example:
b = bytearray("Hello", "utf-8")
b[0] = ord("h")  # Modify the first character
print(b)         # Output: bytearray(b'hello')



# 5. bytes()

# Purpose: Returns an immutable sequence of bytes.
# Syntax: bytes([source, encoding, errors])
# Use Case: Often used in applications that require raw data handling, like network protocols, file I/O, and encoding, where data should remain unaltered.
# Example:
b = bytes("Hello", "utf-8")
print(b)         # Output: b'Hello'
