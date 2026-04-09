# Number Guessing Game

import random

# Computer chooses random number
number = random.randint(1, 100)

print("Guess the number between 1 and 100")

while True:
    guess = input("Enter your guess (or type 'quit'): ")

    if guess.lower() == "quit":
        print("Game ended")
        break

    try:
        guess = int(guess)

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("🎉 Correct! You guessed it!")
            break

    except ValueError:
        print("Invalid input! Enter a number.")