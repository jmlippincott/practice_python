# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
from os import system

while True:
    x = input("Type a single word or phrase:")
    if x.count(" ") > 0:
        word_or_phrase = "phrase"
    else:
        word_or_phrase = "word"
    x_list = list((x.lower()).replace(" ", ""))
    if x_list == x_list[::-1]:
        print(f"\nYour {word_or_phrase} {x} is a palindrome\n")
    else:
        print(f"\nYour {word_or_phrase} {x} is not a palindrome\n")
    input("Press any key to start over")
    system("clear")