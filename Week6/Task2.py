# Implement exception handling in a program that performs complex mathematical calculations, ensuring it handles various potential errors.

def complex_calculation(a, b):
    try:
        result = (a ** 2 + b ** 2) / (a - b)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero occurred.")
    except TypeError:
        print("Error: Invalid input type. Please enter numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        a = float(input("Enter value for a: "))
        b = float(input("Enter value for b: "))
        complex_calculation(a, b)
    except ValueError:
        print("Error: Please enter valid numeric values.")