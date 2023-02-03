import random
print("welcome to the guessing game!!!")

selection = int(input("select difficulty:  "
                      "| Easy = 0 |"
                      " Medium = 1 |"
                      " Hard = 2 | :      "))
print("computer would select a number within range, while you are to guess")
if selection == 0:
    x = 5
elif selection == 1:
    x = 10
elif selection == 2:
    x = 20
elif selection != 0 and selection != 1 and selection != 2:
        select()
def guess():
    mrandom = random.randint(1,x)
    guess = 0
    if mrandom == guess:
        print("Congrats you got it right")
    while mrandom != guess:
        guess = int(input(f"insert your guess within range 1-{x}:  "))
        if guess < mrandom:
            print("your guess is lower")
        elif guess > mrandom:
            print("your guess is higher")
    if mrandom == guess:
        print("Congrats you got it right")
guess()
