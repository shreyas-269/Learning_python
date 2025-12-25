username = input("Enter your username: ")

choice_of_player = input("Enter your choice between snake, water or gun: ") #Taking input from the user
actual_choice_of_user = choice_of_player.lower() #So that even if he writes sNaKe, it is read as snake.

import random
choice_of_python = random.choice(["snake", "water", "gun"]) #Python chooses one of these randomly.

if actual_choice_of_user == "snake":
    if choice_of_python == "snake":
        print("The round ends with a draw as both parties have chosen snake.")
    if choice_of_python == "water":
        print(f"{username} has won as python chose water and {username} has chosen snake.")
    if choice_of_python == "gun":
        print(f"{username} has lost as python chose gun and {username} has chosen snake.")

if actual_choice_of_user == "water":
    if choice_of_python == "snake":
        print(f"{username} has lost as python chose snake and {username} has chosen water.")
    if choice_of_python == "water":
        print("The round ends with a draw as both parties have chosen water.")
    if choice_of_python == "gun":
        print(f"{username} has won as python chose gun and {username} has chosen water.")

if actual_choice_of_user == "gun":
    if choice_of_python == "snake":
        print(f"{username} has won as python chose snake and {username} has chosen gun.")
    if choice_of_python == "water":
        print(f"{username} has lost as python chose water and {username} has chosen gun.")
    if choice_of_python == "gun":
        print("The round ends with a draw as both parties have chosen gun.")
        
    



