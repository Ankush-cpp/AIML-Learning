# Day 8: Input Handling with Exception Handling

while True:
    n = input("Enter a number (or type 'quit' to exit): ")

    if n.lower() == 'quit':
        print("Program ended")
        break

    try:
        num = float(n)

        if num > 0:
            print("Positive number")
        elif num < 0:
            print("Negative number")
        else:
            print("Zero")

    except ValueError:
        print("Invalid input, please enter a number or 'quit'")
