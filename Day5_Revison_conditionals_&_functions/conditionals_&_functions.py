# Day 5: Revision - Conditionals & Functions

# CONDITIONALS --->


num = 10

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# FUNCTIONS --->

def square(x):
    return x * x

print("Square:", square(5))


def check_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(7))