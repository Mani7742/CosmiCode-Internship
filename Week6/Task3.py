# Create a program to read from and write to a JSON file, demonstrating JSON handling in Python.

import json

data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "skills": ["Python", "Data Analysis", "Machine Learning"]
}

# Write data to JSON file
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
print("Data written to data.json")

# Read data from JSON file
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
print("Data read from data.json:")