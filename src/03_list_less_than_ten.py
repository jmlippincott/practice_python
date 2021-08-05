# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

from os import system
import re

def smaller_list(lst):
    global z
    smaller_lst = sorted([int(b) for b in lst if b.isnumeric() if int(b) < z])
    print(f"Your list less than {z} is {smaller_lst}")

while True:
    # takes a list of numbers
    lst = input("Enter a list of numbers in format [#, #, #,...,#]:")
    lst = (re.sub("[\D\s]", ",", lst).split(","))
    system("clear")
    z = int(input("Enter maximum value of return list:"))
    system("clear")
    smaller_list(lst)
    input("Press <Enter> to start over.")
    system("clear")