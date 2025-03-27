#Choose Your Own Adventure

name=input("Enter Your Name: ").upper()
print("Welcome", name,"!\nLet's Make a New Adventure Story!")
again="yes"
while again=="yes":
    ans=input("You are on a DIRT ROAD, it come to an end, you can go LEFT or RIGHT. Which way do you want to go? \n").lower()

    if ans=="left":
        ans=input("You come to a river, you can WALK 🚶around it or SWIM 🏊‍♂️ across it. What do you want to do? \n").lower()
        if ans=="walk":
            ans=input("You face python🐍, you have two weapons to fight it, a SAMURAI sword 🤺 or a SWISS knife 🔪. Which one you choose?\n").lower()
            if ans=="samsurai sword":
                print("WOHOoo! You killed the Python in a single swing!")
            elif ans=="swiss knife":
                print("You died💀 'cuz your weapon was not weaponing in ur hands...")
            else:
                print("Invalid choice. You lose. 😂\n")
        elif ans=="swim":
            print("WOPOS! There were Crocodiles🐊 in the river. You died.💀")
        else:
            print("Invalid choice. You lose.😂\n")

    elif ans=="right":
        ans=input("You face a Bear🐻, you can RUN🏃 or you can CLIMB🧗 a tree. What do you choose?\n").lower()
        if ans=="run":
            print("WOPOS! You Died💀 'cuz the Bear chased and ate you.\n")
        elif ans=="climb":
            print("You are safe now. The Bear eventually leaves and you get down of the tree. ")
            ans=input("Now you face a tribe, who are not good to outsiders. You can try to COMMUNICATE🔊 with them to find your way out or you can jFIGHT🥷 their chief to scare the rest of the tribe. What do you choose?\n").lower()
            if ans=="communicate":
                print("WOPOS! You Died💀. They shot arrows🏹 at you, hundereds of them peircing through you.")
            elif ans=="fight":
                print("WOHOoo! You won the fight against the CHIEF. Now you are the new CHIEF and then you continue to be a dictator😈 there. MWAHAHAHAHAHAHHA!")
            else:
                print("Invalid choice. You lose. 😂")
        else:
            print("Invalid Choice. You lose. 😂")

    else:
        print("Invalid Choice. You lose. 😂")
    
    again=input("Do you want to make another story, YES or NO? : ").lower()