# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.

from os import system
import random

insults = ["Seriously? Do you know what a number is?", "Number...NUMBER....N  U  M  B  E  R.", "No...those are letters.", "Were you dropped on your head as a child?", "Try the buttons at the top of your keyboard.", "I hope you've never voted.", "I bet you pay other people to pick up your food...don't you?", "Have you ever wondered why nobody has ever complimented your intelligence?"]

def check_primality(num):
    factors = [a for a in range(2, num) if num % a == 0]
    if any(factors):
        print(f"{num} is not a prime number. It can be evenly divided by the following factors: {factors}")
    else:
        print(f"{num} is a prime number and has no factors except 1 and {num}.")

while True:
    system("clear")
    number = input("Give me a number and I'll tell you if it's prime or not: ")
    while True:
        if number.isnumeric():
            number = int(number)
            check_primality(number)
            break
        else:
            insult = random.choice(insults)
            system("clear")
            number = input(f"{insult}. Try again: ")

    input("Press Enter to start over.")