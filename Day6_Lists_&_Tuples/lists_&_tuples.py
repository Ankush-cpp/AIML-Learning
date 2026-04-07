# Day 6: Lists & Tuples

# LISTS -->

nums = [1, 2, 3, 4, 5]

# Access
print("First element:", nums[0])

# Add element
nums.append(6)
print("After append:", nums)

# Remove element
nums.remove(3)
print("After remove:", nums)

# Loop
for num in nums:
    print(num)

# Length
print("Length:", len(nums))


# TUPLES ---->

tup = (10, 20, 30, 40)

# Access
print("First element:", tup[0])

# Tuple is immutable (cannot change)
# tup[0] = 100 X will give error

# Loop
for val in tup:
    print(val)

# Length
print("Length:", len(tup))


# PROBLEMS ---->

# Find sum of list
total = 0
for num in nums:
    total += num

print("Sum of list:", total)

# Find max element
max_val = nums[0]
for num in nums:
    if num > max_val:
        max_val = num

print("Max element:", max_val)

# Count occurrences
count = nums.count(2)
print("Count of 2:", count)
