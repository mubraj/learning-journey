#description
#input
#check function
# r>s   s>p  p>r
import random

print("welcome to rock, paper & scissor game")
print("select object")
userInput = (input("for rock input (R), for paper input (P), for scissor input (S):       ")).upper()
comInput = (random.choice(["R", "P", "S"])).upper()

def gameAlgorithm():
      global userInput
      if (userInput == "R" and comInput == "S") or (userInput == "S" and comInput == "P") or (userInput == "P" and comInput == "R"):
            print(f"computer selection is {comInput}")
            print(f"player wins {userInput} > {comInput}")
      elif (comInput == "R" and userInput == "S") or (comInput == "S" and userInput == "P") or (comInput == "P" and userInput == "R"):
            print(f"computer selection is {comInput}")
            print(f"computer wins {comInput} > {userInput}")
      elif userInput == comInput:
            print(f"computer selection is {comInput}")
            print(f"game tie {userInput} = {comInput}")
      else:
            print("invalid input, retry")
            userInput = (input("for rock input (R), for paper input (P), for scissor input (S):       ")).upper()
            gameAlgorithm()


gameAlgorithm()