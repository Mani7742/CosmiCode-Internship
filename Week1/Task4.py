# Implement a program to calculate the area of complex shapes like a trapezoid or an ellipse.

# trapezoid
# a quadrilateral with no sides parallel.

import math

def trapezoid():
    print("Trapezoid Area Calculation:")
    base1 = eval(input("Enter the first base"))
    base2 = eval(input("Enter the second base"))
    height = eval(input("Enter the height"))
    area = 0.5 * base1 * base2 * height
    print(f"Area of Trapezoid is {area}")

# ellipse
# 

def ellipse():
    print("ellipse Area Calculation:")
    major_axis = eval(input("Enter the length of major axis"))
    minor_axis = eval(input("Enter the length of minor axis"))
    area = math.pi * (major_axis/2) * (minor_axis)
    print(f"Area of Ellipse is {area}")


def main():
    print("Complex Shape Area Calculator:")
    print("1. Area of Trapezoid")
    print("2. Area of Ellipse")
    print("3. Exit")

    while True:
        choice = input("Enter Your Choice (1/2/3)")

        
        if choice == "1":
            trapezoid()
        elif choice == "2":
            ellipse()
        elif choice == "3":
            print("Exiting the program")
        else:
            print("Invalid choice. Please Enter (1/2/3)")


if __name__ == "__main__":
    main()