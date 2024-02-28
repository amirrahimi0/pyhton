import math

def is_prime(number):
    """
    Check if a number is prime.

    Args:
    number (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    sqrt_number = int(math.sqrt(number)) + 1
    for i in range(3, sqrt_number, 2):
        if number % i == 0:
            return False

    return True

# Read the start and end of the range
start = int(input())
end = int(input())

# Print all prime numbers in the range
for i in range(start, end + 1):
    if is_prime(i):
        print(i)