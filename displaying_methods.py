def display_options():
    print("1. Start game\n2. Exit game\n")

def print_used_letters(used_letters):
    print("Used letters: ",end="")
    for c in used_letters:
        print(c,end=" ")
    print()

def print_word_user_solution(word_user_solution):
    print("Word: ",end="")
    for c in word_user_solution:
        print(c,end=" ")