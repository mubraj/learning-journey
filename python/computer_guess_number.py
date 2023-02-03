#input no
#computer loop guess
#check guess

import random
ra = int(input("what range should computer guess ( 1 to ?): "))
def guessing(ra):
    com_guess = 0
    list = []
    value = None
    try:
      value = int(input("what value should computer guess:  "))
      if value > ra or value < 1:
          print("value not within range")
          guessing(ra)
      while com_guess != value:
            list.append(com_guess)
            while com_guess in list:
                  com_guess = random.randint(1, ra)
            print (com_guess)
      if com_guess == value:
            print(f"computer guessed the right number |{com_guess}|")
            print(list)
    except:
      print("wrong input, try again")
      guessing(ra)

guessing(ra)