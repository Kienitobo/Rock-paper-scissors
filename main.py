import random
R="Rock"
P="Paper"
S="Scissors"
options=[R,P,S]
possible_actions = ["R", "P", "S"]
computer_action = random.choice(possible_actions)
while True:
    user_action=input("Enter a choice (R, P, S): ")
    if  user_action not in ("R","P","S"):
        print("Error! Please enter an appropriate value.")
    else:
        break
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie! Play again")
    while True:
     user_action=input("Enter a choie(R,P,S): ")
     if user_action not in ("R", "P", "S"):
            print("Error! Please enter an appropriate value")
     else:break
print(f"\nPlayer: {user_action}, CPU: {computer_action}.\n")
        
if user_action == "R":
            if computer_action == "S":
                print("Rock smashes scissors! \n You win!")
                
            else:
                print("Paper covers rock! \n CPU wins.")
                
elif user_action == "P":
            if computer_action == "R":
                print("Paper covers rock! \n You win!")
                
            else:
                print("Scissors cuts paper! \n CPU wins.")
                
elif user_action == "S":
            if computer_action == "P":
                print("Scissors cuts paper! \n You win!")
                
            else:
                 print("Rock smashes scissors! CPU wins.")