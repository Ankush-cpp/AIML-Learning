# Day 2 - Conditions & Loops

## Topics Covered:
- if, elif, else statements
- for loop
- while loop

## Key Learnings:
- Indentation is very important in Python
- The range(start, end) function does not include the end value
- The for loop is used for fixed iterations
- The while loop runs until the condition becomes false
- Always update the variable in a while loop to avoid infinite loops

## Examples:

# Condition Example
a = 10
b = 5

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

# For Loop Example
for i in range(5):
    print(i)

# While Loop Example
i = 1
while i <= 5:
    print(i)
    i += 1