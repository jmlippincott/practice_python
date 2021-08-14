# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
from os import system

while True:
    x = random.randint(1, 9)
    player1 = int(input("Guess a number betwen 1 and 9: "))
    guesses = 1
    if player1 == x:
        input("You have guessed correctly!\nPress enter to start over.")
        system("clear")
    else:
        difference = player1 - x
        if difference >= 1:
            print("Incorrect! Your guess is too high")
        else:
            print("Incorrect! Your guess is too low")
        correct_guess = False
        while correct_guess == False:
            player1 = int(input("Try again: "))
            guesses += 1
            if player1 == x:
                correct_guess = True
                print(f"You have guessed correctly! You took {guesses} guesses")
            else:
                difference = player1 - x
                if difference >= 1:
                    print("Incorrect! Your guess is too high")
                else:
                    print("Incorrect! Your guess is too low")
    input("Press enter to start over.")
    system("clear")