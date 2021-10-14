# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
import random, string

chars = string.ascii_letters + string.digits + string.punctuation

def generate(length):
    psswd = "".join(random.choice(chars) for i in range(length))
    return psswd

while True:
    num = input("How long would you like your new password?  ")
    num = int(num)
    print(generate(num))