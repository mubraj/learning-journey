import random
import string

characters = string.printable
passLength = int(input("input password length:  "))
password = ""
while passLength >= 1:
    passLength -= 1
    choice = random.choice(characters)
    password += choice
    
    
print(password)


#if password should include higher characters
#alphabets
#or strings