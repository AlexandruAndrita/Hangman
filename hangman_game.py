import os
import random
from time import sleep
import displaying_methods
import checking_methods
import unpacking_methods
import accounts

def game(words):
    os.system('cls')
    tries=6
    index=random.randint(0,len(words)-1)

    word=words[index]
    word_user_solution=["_"]*len(word)
    used_letters=[]

    while tries:
        print(f"You have {tries} tries left.")
        displaying_methods.print_used_letters(used_letters)
        displaying_methods.print_word_user_solution(word_user_solution)
        character=input("\nGuess a letter: ")
        if character.isdigit() or checking_methods.isfloat(character):
            print("\nThe character introduced is not a letter\n")
        else:
            # added sleep in order to make more realistic
            sleep(0.6)

            if character not in word:
                tries-=1
            else:
                # if letter exits but already used, number of tries is decreased
                if checking_methods.letter_used_multiple_times(used_letters,character) is True:
                    tries-=1
                else:
                    for i in range(len(word)):
                        if word[i]==character:
                            word_user_solution[i]=character
            used_letters.append(character)

            if checking_methods.check_empty_places(word_user_solution) is False:
                user_solution=""
                for c in word_user_solution:
                    user_solution+=c
                if user_solution==word:
                    break

            print()

    if tries==0:
        print(f"\nNo more tries left. The correct word was '{word}'")
    else:
        print(f"\nYou have guessed the word '{word}' correctly.")

def menu(words,players,file_name_players):
    accounts.add_user(players)

    while True:
        displaying_methods.display_options()
        option=input("Choose an option: ")
        os.system('cls')

        # for a more realistic experience
        print("Loading...")
        sleep(1.5)

        try:
            option=int(option)
            if option == 1:
                while True:
                    game(words)
                    displaying_methods.play_another_round()
                    option=input("Do you want to play another round: ")

                    try:
                        option=int(option)
                        if option == 2:
                            unpacking_methods.add_new_users(players,file_name_players)
                            os.system('cls')
                            print("You have exited the game")
                            exit(0)
                        elif option!=1:
                            os.system('cls')
                            print("The value introduced is not valid\n")
                        else:
                            os.system('cls')
                            accounts.add_user(players)
                    except ValueError:
                        os.system('cls')
                        print("The value introduced is not a number\n")

            elif option == 2:
                unpacking_methods.add_new_users(players,file_name_players)
                os.system('cls')
                print("You have exited the game")
                exit(0)
            else:
                os.system('cls')
                print("The value introduced is not valid\n")
        except ValueError:
            os.system('cls')
            print("The value introduced is not a number\n")


if __name__=='__main__':
    file_name_words="words.txt"
    file_name_players="existing_users.txt"
    players=unpacking_methods.unpack_users(file_name_players)
    words=unpacking_methods.unpack_words(file_name_words)
    print("\n\t\tHANGMAN\n")
    menu(words,players,file_name_players)