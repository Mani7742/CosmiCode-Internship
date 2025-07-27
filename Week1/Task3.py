# Write a program that takes user input for three numbers and prints the largest and smallest among them.

a = eval(input("Enter the First Number: "))
b = eval(input("Enter the Second Number: "))
c = eval(input("Enter the Third Number: "))

if (a>b and a>c):
    print(f"{a} is the Largest Number")
elif(b>a and b>c):
    print(f"{b} is the largest Number")
else:
    print(f"{c} is the Largest Number")



if (a<b and a<c):
    print(f"{a} is the Largest Number")
elif(b<a and b<c):
    print(f"{b} is the largest Number")
else:
    print(f"{c} is the Largest Number")