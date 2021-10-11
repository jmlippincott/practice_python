# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

from os import system
from faker import Faker

def show_full(how_many):
    global full_list
    fake = Faker()
    for i in range(how_many):
        one_more = fake.first_name()
        full_list.append(one_more)
    return full_list

def remove_dupes(lst):
    global full_list
    lst = set(lst)
    lst = list(lst)
    lst.sort()
    full_list = lst

while True:
    full_list = []
    how_many = input("How many names in full random list?")
    how_many = int(how_many)
    print(f"There are {how_many} entries in the full list of names. The full list of names is \n{show_full(how_many)}")
    input("Press Enter to remove duplicates and sort the list.")
    remove_dupes(full_list)
    print(f"The refined list of names includes {len(full_list)} entries. The pared list of names is \n{full_list}")