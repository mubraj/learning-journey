import random
import string
from catalog import words

lettersSet = set(string.ascii_lowercase)
usedLetter = set()
word = None
wordSet = None

def wordSelection(words):
    global word
    global wordSet
    word  = random.choice(words).lower()
    while ' '  in word or '-' in word:
        word  = random.choice(words).lower()
    wordSet = set(word)
    return wordSet

def inputLetter():
    global word
    global wordSet
    global lettersSet
    print(f"{word}") #check
    live = len(word) + 6
    while len(wordSet) > 0 and live > 0:
        live -= 1
        print(f"you have {live} lives, you have used these letters: ", ' '.join(usedLetter))
        x = [characters if characters in usedLetter else "-" for characters in word]
        print("current word: ",' '.join(x))
        letterChoice = input("input guess alphabet:  ").lower()
        if letterChoice in lettersSet and letterChoice not in usedLetter:
            usedLetter.add(letterChoice)
            if letterChoice in wordSet:
                wordSet.remove(letterChoice)
        elif letterChoice in usedLetter:
            print("sorry, alphabet has been used")
        elif letterChoice not in lettersSet or len(letterChoice) >= 2:
            print("sorry wrong input")
    if live == 0:
        print(f"you died. the word is {word}")
    else:
        print(f"you guessed the correct word: {word}")

wordSelection(words)
inputLetter()   