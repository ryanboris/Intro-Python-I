def is_prime(num):
    """
    neg. numbers are not prime numbers
    0 && 1 are not prime numbers
    2 is the first prime number
    prime numbers will return 0 for only num % 1 and num % num (can only give a remainder of 0 when divided by 1 `boring` and itself)

    pseudocode:
        - if num is either < 0, 0, or 1 - return false
        - all even numbers, except for 2, can't be prime numbers since by definition even numbers would give 0 for %1, %2, and %num

    """
    if num >= 2:
        for i in range(2, num):
            if not (num % i):
                return False
    else:
        return False
    return True


print(is_prime(1))
print(is_prime(2))
print(is_prime(4))
print(is_prime(7))
print(is_prime(-2))
