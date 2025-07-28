# Implement a program to find all the prime factors of a given number.
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 2:
        factors.append(n)
    return factors
if __name__ == "__main__":
    number = int(input("Enter a number to find its prime factors: "))
    factors = prime_factors(number)
    print(f"Prime factors of {number} are: {factors}")
