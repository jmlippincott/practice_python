# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

from os import system

def fibonacci(num):
    seq = [0, 1]
    for i in range(-1, (num - 3)):
        next = seq[i+1] + seq[i+2]
        seq.append(next)
    return seq[:num]

while True:
    count = ""
    while not count.isnumeric():
        count = input("How many Fibonacci numbers would you like me to generate?")
        system("clear")
    print(f"{fibonacci(int(count))}")
    input("Press 'Enter/Return' to start over")
    system("clear")