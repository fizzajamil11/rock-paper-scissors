import random
item_list=["paper","scissor","rock"]

user_choice=input("Enter your move = Rock , Paper , Scissor = ")
comp_choice=random.choice(item_list)

print(f"user choice = {user_choice} , computer choice = {comp_choice}")

if user_choice==comp_choice:
    print("Both choices same: = Match Tie..")

elif user_choice=="rock":
    if comp_choice=="paper":
        print("Paper covers Rock = Computer win")
    else:
        print("Rock smahes Scissor = You win")

elif user_choice=="paper":
    if comp_choice=="scissor":
        print("Scissor cuts Paper = Computer win")
    else:
        print("Paper covers Rock = You win")

elif user_choice=="scissor":
    if comp_choice=="paper":
        print("Scissor cuts Paper = You win")
    else:
        print("Rock smahes Scissor = Computer win")