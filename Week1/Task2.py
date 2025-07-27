def power(base, exponent):
    """Calculate the power of a number."""
    return base ** exponent

def modulo(dividend, divisor):
    """Calculate the remainder of division."""
    return dividend % divisor

def is_number(value):
    """Check if the input can be converted to a float."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def main():
    print("Advanced Arithmetic Operations Calculator")
    print("1. Power (x^y)")
    print("2. Modulo (x % y)")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1/2/3): ")
        
        if choice == '1':
            base = input("Enter the base: ")
            exponent = input("Enter the exponent: ")
            if is_number(base) and is_number(exponent):
                result = power(float(base), float(exponent))
                print(f"{base}^{exponent} = {result}")
            else:
                print("Invalid input. Please enter numbers only.")
        
        elif choice == '2':
            dividend = input("Enter the dividend: ")
            divisor = input("Enter the divisor: ")
            if is_number(dividend) and is_number(divisor):
                if float(divisor) == 0:
                    print("Error: Divisor cannot be zero.")
                else:
                    result = modulo(float(dividend), float(divisor))
                    print(f"{dividend} % {divisor} = {result}")
            else:
                print("Invalid input. Please enter numbers only.")
        
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()