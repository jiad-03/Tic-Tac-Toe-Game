#number guessing game

import random

tr=input("Enter the higher range: ")

if tr.isdigit():
    tr= int(tr)
    if tr<=0:
        print("Enter Number Greater than Zero/0")
        quit()
else:
    print("Invalde Entery...Enter a Number.")
    quit()
r=random.randint(0,tr)#includes tr
guess_count=0
while True:
    guess_count+=1
    user_guess=input("Guess the Number...")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Invalde Entery...Enter a Number.")
        continue
    if user_guess==r:
        print("BINGO!")
        break
    
    elif user_guess>r:
        print("You guessed a number Greater than the RANDOM Number...")

    else:
        print("You guessed a number Less than the RANDOM number...")

print("You got the right answer in",guess_count,"guesses.")

