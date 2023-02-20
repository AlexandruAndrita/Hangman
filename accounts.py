import os
from checking_methods import username_exists

def add_user(players):
    username=input("Enter a name to play with: ")

    while True:
        if username_exists(username,players) is False:
            break
        os.system('cls')
        print(f"The username {username} already exists. Please enter another one")
        username=input("Name: ")

    players.append(username)

