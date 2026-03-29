# Day 4: Strings

# STRINGS --->

text = "Python"

# Access characters
print("First character:", text[0])
print("Last character:", text[-1])

# Slicing
print("First 3 chars:", text[:3])
print("Reverse:", text[::-1])

# String functions
sentence = "python programming"

print("Upper:", sentence.upper())
print("Lower:", sentence.lower())
print("Length:", len(sentence))

# Replace
print("Replace:", sentence.replace("python", "Java"))

# Check substring
print("Contains 'python':", "python" in sentence)

# PROBLEMS --->

# Reverse a string
s = "hello"
print("Reversed:", s[::-1])

# Palindrome check
word = "madam"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Count vowels
count = 0
for char in sentence:
    if char in "aeiou":
        count += 1

print("Vowel count:", count)