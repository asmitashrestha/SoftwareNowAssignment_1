"""
# Student Name: Sabina B K
# Student Id: 397686
# Group DAN/EXT 14

# Write a program that finds all prime numbers up to a given limit (maximum 100), and display:
# the total count of prime numbers found:
# the smallest and largest prime number in the range:
# the sum of all prime numbers found:
"""

# Function to check whether a number is prime
def is_prime(n):
    # Prime numbers must be 2 or greater
    if n < 2:
        return False

    # To check if n is divisible by any number from 2 upto square root n
    # If divisible, it is NOT a prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:   # If remainder is 0 then not prime
            return False

    # If no divisors found, number is prime
    return True


# To ask user for a limit (maximum value to check)
limit = int(input("Enter a limit (max 100): "))

# To create a list of prime numbers from 2 up to the limit 
primes = [n for n in range(2, limit + 1) if is_prime(n)]

# To print all prime numbers found
print("Prime numbers found:", *primes) # The * before primes prints the list without brackets

# To print the total number of prime numbers found
print("Total primes found:", len(primes))

# To print the largest prime (last element)
print("Largest prime:", primes[-1] if primes else "None")

# To print the smallest prime (first element)
print("Smallest prime:", primes[0] if primes else "None")

# To print the sum of all prime numbers
print("Sum of all primes:", sum(primes))
