
"""
@author: Andrew Daly

The purpose of this code is for a homework assignment for the course Computational Thinking.
This code is an interactive game between the computer and user. The user establishes a range
of numbers in which case the computer must guess the number the user is thinking of. The user 
enters comparison operators to signify a larger, smaller or correct number the computer guessed.
The game ends when the correct number is guessed or the user provides inaccurate feedback.

"""

import math

print("Think of a number between two numbers and I'll guess it.")
lower = int(input("Enter the smaller number: "))
upper = int(input("Enter the larger number: "))

min_guesses = math.ceil(math.log2(upper - lower + 1))

guesses = 0
while guesses < min_guesses:
    guess = (lower + upper) // 2
    print(lower, upper)
    response = input("Your number is " + str(guess) + "\nEnter =, <, or >: ")
    if response == "=":
        print("Hooray, I've got it in", guesses+1, "tries!")
        break
    elif response == "<":
        upper = guess - 1
    elif response == ">":
        lower = guess + 1
    guesses += 1
else:
    print("I'm out of guesses, and you cheated.")

