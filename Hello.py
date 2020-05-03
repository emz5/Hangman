import random

wordlist = list()
wordlist = [word.rstrip("\n") for word in open("Hangman_Words.txt")]
index = random.randint(0, len(wordlist) - 1)
number = 1
while "Emily" != wordlist[index]:
    print(wordlist[index] + "(", number, ")")
    index = random.randint(0, len(wordlist) - 1)
    number = number + 1
print("Emily has been found")
