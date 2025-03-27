#Rock Paper Scissors

import random as rand

user_wins=0
comp_wins=0
options=["rock", "paper", "scissors"]
while True:
    user_input=input("You pick: Rock🪨 /Paper📄 /Scissors ✂️ or Wanna Quit❌(Q)? : \n").lower()
    if user_input=="q":
        break
    
    if user_input not in options:
        print("Pick That is in the option man 🥸 !")
        continue
    r=rand.randint(0,2)
    #0->rock, paper->1, scissors->2
    comp_pick=options[r]
    print("I pick ", comp_pick)

    if user_input=="rock" and comp_pick=="scissors":
        print("Luck might be on your side...for now 😈 \n")
        user_wins+=1
        continue
    elif user_input=="paper" and comp_pick=="rock":
        print("Luck might be on your side...for now 😈\n")
        user_wins+=1

    elif user_input=="scissors" and comp_pick=="paper":
        print("Luck might be on your side...for now 😈\n")
        user_wins+=1
    elif user_input==comp_pick:
        print("WOOPS😭 ! Pick Again...\n")
    else:
        print("HAHA...You Lost😂...better luck next time!\n")
        comp_wins+=1

print("You won",user_wins,"times")
print() 
print("I won",comp_wins,"times") 
print()   
print("Goodbye, Loser ;)...")