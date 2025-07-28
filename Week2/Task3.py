# Write a function to calculate the greatest common divisor (GCD) and least common multiple (LCM) of two numbers.
def compute_gcd(a,b):
    while b != 0:
        a,b = b , a%b
    return a

def compute_lcm(a, b):
    gcd_value = compute_gcd(a, b)
    lcm_value = (a * b) // gcd_value
    return lcm_value

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    gcd_result = compute_gcd(num1, num2)
    lcm_result = compute_lcm(num1, num2)
    
    print(f"GCD of {num1} and {num2} is: {gcd_result}")
    print(f"LCM of {num1} and {num2} is: {lcm_result}")