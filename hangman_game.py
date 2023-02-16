import os
import random
from time import sleep
import displaying_methods
import checking_methods


def unpack_words(path):
    words=[]
    try:
        with open(path,"r") as f:
            words=f.readlines()
        for i in range(len(words)):
            if words[i][-1]=='\n':
                words[i]=words[i][:-1]
    except FileNotFoundError:
        raise FileNotFoundError("File does not exist")
    return words

def game(words):
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

def menu(words):

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
                game(words)
                exit(0)
            elif option == 2:
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
    file_name="words.txt"
    words=unpack_words(file_name)
    print("\n\t\tHANGMAN\n")
    menu(words)