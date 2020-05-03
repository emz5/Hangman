import mysql.connector
import dns.resolver
import random
#import readchar
# get the list of words from Hangman Wrod list
wordlist = list()
valid = False
cnx = mysql.connector.connect(host='localhost', database='CGS', user='root', passwd='G0lfer01!')
cursor = cnx.cursor()
query =("SELECT StudentId, StudentFirstName FROM Student")
cursor.execute (query)
for (StudentId, StudentFirstName) in cursor:
    print ('{}, {}'.format(StudentId, StudentFirstName))
cursor.close()
cnx.close()
print("Please select a category: 1) Food, 2) Sports")
while valid == False:
    cat = input()
    #print(cat)
    if cat == "1":
        wordlist = [word.rstrip("\n") for word in open("Food.txt")]
        valid = True
    if cat == "2":
        wordlist = [word.rstrip("\n") for word in open("Sports.txt")]
        valid = True
# get random words' letters
# letters --> _ _ _
index = random.randint(0, len(wordlist) - 1)
originalWord = wordlist[index]
guess = ""
for i in range(len(originalWord)):
    guess += "_"

# times played 0
# print out the _ _ _...
# entered _
number = len(originalWord)
gameover = False
while guess != originalWord and not gameover:
    printWord = ""
    for c in guess:
        printWord += c + " "
    print ('{}({})'.format(printWord,number))
#     print '{}, {}'.format(StudentId, StudentFirstName)
    # input letter + hit 'enter' key
    print ("Please guess a letter: You have {} guesses".format(number))
    key = input()
    if key.lower() == originalWord.lower():
        gameover = True
    else:
        print("You entered: ", key[0])

    # if entered is ?
    # first spot _ with get uncovered
    # shows how many guesses left
    j = 0
    newguess = ""
    for j in range(len(originalWord)):
        if key == originalWord[j] or (key[0] == "?" and guess[j] == "_"):
            newguess += originalWord[j]
        else:
            newguess += guess[j]
    guess = newguess
    number = number - 1

    # if entered is . or you guess more times the there are letters
    # gameover --> you lose
    if key[0] == "." or number == 0:
        gameover = True
if newguess == originalWord:
    print("Congradulations! It's ", originalWord)
print("You played ", len(originalWord) - number, "times", originalWord)
