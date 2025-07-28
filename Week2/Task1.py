# Write a program to check if a number is prime, and also list all prime numbers up to that number.
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1 , 2):
        if n % i == 0:
            return False
    return True

def list_primes_up_to(n):
    primes = []
    for i in range(2,n+1):
        if is_prime(i):
            primes.append(i)
    return primes

if __name__ == "__main__":
    number = int(input("Enter the Number:"))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

    primes_up_to_number = list_primes_up_to(number)
    print(f"Prime numbers up to {number}: {primes_up_to_number}")