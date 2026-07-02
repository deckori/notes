def is_prime(num):
    # Step 1: Handle Numbers less than or equal to 1 as not prime
    if num <= 1:
        return False
    # Step 2: Loop through to check divisors from 2 to num
    for i in range(2, num):
        # Step 3:If Divisible: If the remainder is 0, it’s not prime
        if num % i == 0:
            return False
    # Step 4: If no divisors are found, its prime
    return True


# Testing code
print(is_prime(25))  # Expected output: False
print(is_prime(29))  # Expected output: True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
