# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.

from os import system

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
            system("clear")
            number = input("Nope, that's not a number.  Try again: ")

    input("Press Enter to start over.")