# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
# 1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# 2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
import datetime
from os import system
import time

name = input("Please tell me your name: ")
age = int(input("Please tell me your age: "))
hundred = (datetime.date.today()).year - age + 100
system("clear")

response = f"Pleasure to meet you {name}.\nYou will turn 100 years old in {hundred}"
print(response)

time.sleep(3)
copies = int(input("Enter any whole number between 1 and 20: "))
system("clear")
print(copies * response)
