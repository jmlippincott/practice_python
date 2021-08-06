# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random
from os import system
from simple_term_menu import TerminalMenu

choices = ['Rock', 'Paper', 'Scissors']

def menu():
    global player1
    options = choices
    menu_title = "Choose your weapon!"
    cursor = "} "
    cursor_style = ("fg_purple", "bold")
    menu_style = ("fg_yellow", "bg_red")
    terminal_menu = TerminalMenu(options, title="Choose your weapon!", menu_cursor_style=cursor_style, menu_cursor=cursor, menu_highlight_style=menu_style)
    menu_entry_index = terminal_menu.show()
    player1 = options[menu_entry_index]

def evaluate_choices(a, b):
    if a == b:
        return print("It's a tie!")
    elif a == 'Rock':
        if b == 'Paper':
            return print("Computer wins!")
        else:
            return print("You win!")
    elif a == 'Paper':
        if b == 'Scissors':
            return print("Computer wins!")
        else:
            return print("You win!")
    elif a == 'Scissors':
        if b == 'Rock':
            return print("Computer wins!")
        else:
            return print("You win!")

while True:
    menu()
    input(f"\nYour selection is {player1}\nPress any key to continue")
    computer = random.choice(choices)
    input(f"\nComputer chooses {computer}\nPress any key to continue\n")
    evaluate_choices(player1, computer)
    input("\nPress any key to continue")
    system("clear")
