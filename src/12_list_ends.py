# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

from os import system
import random

lst_length = random.randint(1,100)
lst = [random.randint(0,100) for i in range(lst_length)]
print(lst)
lst.sort()
lst = [lst[0], lst[-1]]