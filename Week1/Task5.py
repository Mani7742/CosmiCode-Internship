# Create a program that converts a given time in seconds to hours, minutes, and seconds.

total_seconds = int(input("Enter Time in Seconds"))

hours = total_seconds//3600
remaining_seconds  = total_seconds%3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{total_seconds} seconds = {hours} hours, {minutes} minutes, and {seconds} seconds")