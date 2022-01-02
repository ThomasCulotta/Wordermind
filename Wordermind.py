import random, re

filename = "dict.txt"
with open(filename, "r") as file:
    words = file.readlines()

prntReset = "\033[0m"
prntBold = "\033[01m"
prntGreen = "\033[32m"
prntYellow = "\033[93m"
prntGrey = "\033[90m"
prntBlock = "█"

maxChances = 6
chancesTaken = 6
keyWord = random.choice(words).strip()
resultBoard = []

print("Guess the 5 letter word. 6 guesses.\n")

for chance in range(1, maxChances + 1):
    guessWord = input().lower()

    while re.match("[a-z]{5}", guessWord) == None:
        print("Invalid word. Try again: ", end="")
        guessWord = input().lower()

    result = ""
    for index in range(5):
        if guessWord[index] == keyWord[index]:
            print(prntBold + prntGreen + guessWord[index].upper() + prntReset, end="")
            result += prntGreen + prntBlock + prntReset
        elif guessWord[index] in keyWord:
            print(prntBold + prntYellow + guessWord[index].upper() + prntReset, end="")
            result += prntYellow + prntBlock + prntReset
        else:
            print(prntGrey + guessWord[index] + prntReset, end="")
            result += prntGrey + prntBlock + prntReset

    resultBoard.append(result)
    print()

    if guessWord == keyWord:
        chancesTaken = chance
        break

print()

if chancesTaken == 6:
    print(prntBold + keyWord + prntReset)
    print()

print(f"{chancesTaken}/{maxChances}")

for result in resultBoard:
    print(result)
