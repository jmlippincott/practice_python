# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
from os import system

no = ["Nope!", "Nein!", "Nyet!", "Wrongo!", "Are you even trying?", "C'mon, man...", "That's not even kinda close.", "Missed it by thaaat much."]
dumb = ["Seriously? Do you know what a number is?", "Number...NUMBER....N  U  M  B  E  R.", "No...those are letters.", "Were you dropped on your head as a child?", "Try the buttons at the top of your keyboard.", "I hope you've never voted.", "I bet you pay other people to pick up your food...don't you?", "Have you ever wondered why nobody has ever complimented your intelligence?"]

while True:
    system("clear")
    guesses = 0
    correct_guess = False
    x = random.randint(1, 9)
    player1 = input("Guess a number between 1 and 9: ").lower()
    while correct_guess == False:
        while not player1.isnumeric():
            if player1 == 'exit':
                break
            else:
                insult = random.choice(dumb)
                player1 = input(f"{insult} Guess a number between 1 and 9: ").lower()
        if player1 == 'exit':
            break
        player1 = int(player1)
        guesses += 1
        wrong = random.choice(no)
        if player1 == x:
            print(f"You have guessed correctly! You took {guesses} guesses")
            correct_guess = True
        elif player1 > x:
            player1 = input(f"{wrong} Your guess is too high.\nTry again: ").lower()
        else:
            player1 = input(f"{wrong} Your guess is too low.\nTry again: ").lower()
    if player1 == "exit":
        print("Goodbye!")
        break
    else:
        player1 = input("Press Enter to continue or type 'Exit' to exit.").lower()
    if player1 == "exit":
        print("Goodbye!")
        break
    else:
        system("clear")