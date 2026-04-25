# -------- Q1: File Write + Read --------

with open("names.txt", "w") as f:
    for i in range(5):
        name = input("Enter name: ")
        f.write(name + "\n")

with open("names.txt", "r") as f:
    print("Names in file:")
    print(f.read())


# -------- Q2: Append Mode --------

with open("log.txt", "a") as f:
    f.write("Program run successfully\n")

with open("log.txt", "r") as f:
    print("Logs:")
    print(f.read())


# -------- Q3: List Comprehension --------

nums = [5, 10, 15, 20, 25]

new_list = [x for x in nums if x > 15]
print("Filtered list:", new_list)


# -------- Q4: JSON Handling --------

import json

cities = {
    "Delhi": 20000000,
    "Mumbai": 18000000,
    "Bangalore": 12000000
}

# Save to file
with open("cities.json", "w") as f:
    json.dump(cities, f)

# Load file
with open("cities.json", "r") as f:
    data = json.load(f)

print("Cities data:", data)

# Update
city = input("Enter new city: ")
pop = int(input("Enter population: "))

data[city] = pop

with open("cities.json", "w") as f:
    json.dump(data, f)


# -------- Q5: Exception Handling --------

try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")