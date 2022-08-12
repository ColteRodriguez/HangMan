import random

# entering a word
wordsBank = []
TheWord = input("Player 1, type a word")
wordsBank.append(TheWord)
for i in range(10):
    print("------------------------------------")

# picking a random word to use and storing its length
goalWord = wordsBank[random.randint(0, (len(wordsBank) - 1))]

# iterating through the number of letters in the chosen word and printing the length in __...
wordblanks = []
for i in range(len(goalWord)):
    wordblanks.append("_")
print(str(wordblanks))

# store the user guesses in array because apparently global variables just don't exist in python
guessArray = []
badGuessArray = []


def guessfxn():
    guessArray.append(input("guess a letter: "))

# if the word is still incomplete, run the guess function, then check to see if the goal word contains the guessed
# letter. If the guessed letter is in the word, show where the letter is located and how many times it appears. If the
# guess is not in the word, tell the player that the guess appears 0 times, then run the guess function again.


while wordblanks.__contains__('_'):
    guessfxn()
    if goalWord.__contains__(guessArray[len(guessArray)-1]):
        times = 0
        for i in range(len(goalWord)):
            if goalWord[i] == guessArray[len(guessArray)-1]:
                wordblanks.pop(i)
                wordblanks.insert(i, guessArray[len(guessArray)-1])
                times = times + 1
        print("the mystery word contains the letter", guessArray[len(guessArray)-1], times, "times")
        print(wordblanks)
    else:
        print("the mystery word contains the letter", guessArray[len(guessArray)-1], " 0 times. Guess again")
        print(wordblanks)
        badGuessArray.append(guessArray[len(guessArray)-1])
        if len(badGuessArray) > 5:
            print("you lose")

if not wordblanks.__contains__('_'):
    print("you win!")
