# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

from os import system
import time

while True:
    num = int(input("Enter any number:"))
    system("clear")
    divisors = [b for b in range(2, num) if num % b == 0]
    if any(divisors):
        print(f"The number you entered was {num}\n\nThe divisors for {num} are {divisors}")
    else:
        print(f"Your number {num} is a prime number and does not have any divisors")

    time.sleep(3)

    input("Press any key to restart")
    system("clear")