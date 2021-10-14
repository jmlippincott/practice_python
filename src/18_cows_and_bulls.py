import random, string
from os import system

chars = string.digits

def generate(digits):
    return list("".join(random.choice(chars) for i in range(digits)))

while True:
    num_digits_solution = int(input("Enter puzzle size (0-9):  "))
    solution = generate(num_digits_solution)
    # print(f"Solution: {solution}") #uncomment to debug
    guesses = 0
    correct = False
    while correct == False:
        guesses += 1
        bulls = 0
        cows = 0
        guess = list(input(f"Please enter a {num_digits_solution} digit guess:  "))
        for i in range(num_digits_solution):
            if guess[i] == solution[i]:
                bulls += 1
            else:
                cows += 1
        if bulls == num_digits_solution:
            correct = True
        else:
            print(f"Bulls: {bulls}\nCows: {cows}\nGuesses: {guesses}")
    input(f"Your solution {guess} is correct! Please press <Enter> to start over.")
    system("clear")