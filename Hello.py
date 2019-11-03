import random

wordlist = list()
wordlist = [word.rstrip("\n") for word in open("Hangman_Words.txt")]
index = random.randint(0, 212)
print(wordlist[index])
