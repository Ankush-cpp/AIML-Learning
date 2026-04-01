# Day 7: Dictionaries

# DICTIONARY --->

student = {
    "name": "Ankush",
    "age": 20,
    "course": "AI/ML"
}

# Access values
print("Name:", student["name"])

# Add new key
student["city"] = "Delhi"
print("After adding city:", student)

# Update value
student["age"] = 21
print("Updated age:", student)

# Remove key
student.pop("course")
print("After removal:", student)

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)


# METHODS --->

print("Keys:", student.keys())
print("Values:", student.values())


# PROBLEMS -->

# Count frequency of elements
nums = [1, 2, 2, 3, 3, 3]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency:", freq)