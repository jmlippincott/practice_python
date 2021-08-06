# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

import random
from os import system

while True:
    input("Press any key to generate a random list of numbers")
    lst = sorted(list(set([random.randrange(0, 50, 1) for i in range(random.randint(1, 21))])))
    input(f"{lst}\nPress any key to filter list for only even numbers")
    lst_even = [a for a in lst if a % 2 == 0]
    if any(lst_even):
        print(f"\nThe even numbers from the list are {lst_even}")
    else:
        print(f"\nThere are no even numbers in this list")
    input(f"\nPress any key to start over")
    system("clear")