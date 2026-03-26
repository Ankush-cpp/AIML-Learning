# Day 3: Functions & Lists

# FUNCTIONS -->

def greet(name):
    return "Hello " + name

print(greet("Ankush"))


def add(a, b):
    return a + b

print("Sum:", add(5, 3))


# LISTS -->

nums = [1, 2, 3, 4, 5]

# Access
print("First element:", nums[0])

# Add element
nums.append(6)

# Remove element
nums.remove(3)

# Loop through list
for num in nums:
    print(num)