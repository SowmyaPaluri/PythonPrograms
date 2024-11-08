# twin primes in range 1 and b 


import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(a, b):
    twin_primes = []
    for num in range(a, b - 1):  # b - 1 to prevent out of range for (num, num+2)
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes

# Example usage
a = 10
b = 50
print(find_twin_primes(a, b))

    
    
    
    
    
    
a,b = int(input("Enter 2 numbers with space separated: "))