import random, re

filename = "dict.txt"
with open(filename, "r") as file:
    words = [word.strip() for word in file.readlines()]

prntReset = "\033[0m"
prntBold = "\033[01m"
prntGreen = "\033[32m"
prntYellow = "\033[93m"
prntGrey = "\033[90m"
prntBlock = "█"

maxChances = 6
chancesTaken = 7
keyWord = random.choice(words)
resultBoard = []

print(keyWord)
print("Guess the 5 letter word. 6 guesses.\n")
for chance in range(maxChances):
    guessWord = input().lower()
    resultBoard.append([prntBlock for index in range(5)])

    while guessWord not in words:
        print("Not in word list. Try again: ", end="")
        guessWord = input().lower()

    guessingWord = list(guessWord)
    searchingWord = list(keyWord)
    printWord = ["." for index in range(5)]

    # Find correct letters
    for index in range(5):
        if guessingWord[index] == searchingWord[index]:
            printWord[index] = prntBold + prntGreen + guessingWord[index].upper() + prntReset
            resultBoard[chance][index] = prntGreen + prntBlock + prntReset
            searchingWord[index] = "."
            guessingWord[index] = "."

    # Find out of place letters
    for index in range(5):
        if guessingWord[index] == ".":
            continue

        if guessingWord[index] in searchingWord:
            if guessingWord[index + 1:].count(guessingWord[index]) < searchingWord.count(guessingWord[index]):
                printWord[index] = prntBold + prntYellow + guessingWord[index].upper() + prntReset
                resultBoard[chance][index] = prntYellow + prntBlock + prntReset
                guessingWord[index] = "."

    # Wrong letters
    for index in range(5):
        if guessingWord[index] == ".":
            continue

        printWord[index] = prntGrey + guessingWord[index] + prntReset
        resultBoard[chance][index] = prntGrey + prntBlock + prntReset

    print("".join(printWord) + f" {chance + 1}/{maxChances}")

    if guessWord == keyWord:
        chancesTaken = chance + 1
        break

print()

if chancesTaken == 7:
    print(prntBold + keyWord + prntReset)
    print()
else:
    print(f"{chancesTaken}/{maxChances}")

for result in resultBoard:
    print("".join(result))
