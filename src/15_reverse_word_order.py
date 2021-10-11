# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.

def backwards(sentence):
    sentence = sentence.split(" ")
    sentence.reverse()
    sentence = " ".join(sentence)
    return sentence

while True:
    phrase = input("Provide a multiword phrase and I will repeat it in reverse order:  ")
    print(backwards(phrase))