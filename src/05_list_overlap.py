# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

import random
from os import system

while True:
    input("Press any key to generate lists")
    lst1 = sorted(list(set([random.randrange(0, 50, 1) for i in range(random.randint(1, 21))])))
    lst2 = sorted(list(set([random.randrange(0, 50, 1) for i in range(random.randint(1, 21))])))
    print(f"\n\nList 1 = {lst1}\n\nList 2 = {lst2}\n\n")
    input("Press any key to generate list of elements common to Lists 1 & 2\n\n")
    common = [a for a in lst1 if lst2.count(a) > 0]
    if any(common):
        print(f"These characters, {common}, are common to both Lists 1 & 2\n\n")
    else:
        print("There are no common elements between Lists 1 & 2\n\n")
    input("Press any key to start over")
    system("clear")
