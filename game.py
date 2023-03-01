from tkinter import *
import random

import unpacking_methods
import checking_methods

def disable_event():
    pass

window=Tk()
window.title("Hangman")
window.geometry("450x450")
window.resizable(0,0)
window.protocol("WM_DELETE_WINDOW",disable_event)
window.configure(bg="gray70")

frame_title=Frame(window)
label_title=Label(frame_title,text="The Hangman",justify=LEFT,font=('Arial',25),bg="gray70",fg="black")
label_title.pack(side=LEFT)
frame_title.pack(padx=1,pady=1)

def character(c,word,word_user_solution,tries_label,word_label,win):
    global tries

    if tries==1:
        #for wid in win.winfo_children():
            #wid.destroy()
        win.destroy()
        verdict_window=Toplevel(window)
        verdict_window.geometry("450x450")
        verdict_window.configure(bg="gray70")

        correct_word=Label(verdict_window,text=f"You lost\n\nCorrect word was: {word}",font=('Arial'),pady=15,bg="gray70")
        correct_word.pack(padx=15)

        message=Label(verdict_window,text="Do you want to play again?\nClose this window",font=('Arial'),pady=25,bg="gray70")
        message.pack(padx=15)

        tries=6
        tries_label.configure(text=f"Tries left: {tries}",bg="gray70")

    if c not in word:
        tries-=1
        tries_label.configure(text=f"Tries left: {tries}",bg="gray70")
    else:
        for i in range(len(word)):
            if word[i]==c:
                word_user_solution[i]=c
        result=""
        user_sol=""
        for c in word_user_solution:
            result=result+c+"  "
            user_sol=user_sol+c
        if word==user_sol:
            #for wid in win.winfo_children():
                #wid.destroy()
            win.destroy()
            verdict_window=Toplevel(window)
            verdict_window.geometry("450x450")
            verdict_window.configure(bg="gray70")

            endgame_label=Label(verdict_window,text=f"Congratulations\n\nYou guessed the correct word: {word}",font=('Arial'),pady=15,bg="gray70")
            endgame_label.pack(padx=15)

            message = Label(verdict_window, text="Do you want to play again?\nClose this window", font=('Arial'), pady=25,bg="gray70")
            message.pack(padx=15)

            tries=6
            tries_label.configure(text=f"Tries left: {tries}")
            tries_label.configure(bg="gray70")
        else:
            word_label.configure(text=result,bg="gray70")

def create_buttons(win,new_button_frame,word,word_user_solution,tries_label,word_label):
    button = Button(new_button_frame, text="A", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('a',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=0, column=0)

    button = Button(new_button_frame, text="B", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('b',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=0, column=1)

    button = Button(new_button_frame, text="C", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('c',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=0, column=2)

    button = Button(new_button_frame, text="D", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('d',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=0, column=3)

    button = Button(new_button_frame, text="E", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('e',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=0, column=4)

    button = Button(new_button_frame, text="F", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('f',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=0, column=5)

    button = Button(new_button_frame, text="G", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('g',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=0, column=6)

    button = Button(new_button_frame, text="H", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('h',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=0, column=7)

    button = Button(new_button_frame, text="I", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('i',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=0, column=8)

    button = Button(new_button_frame, text="J", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('j',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=0, column=9)

    button = Button(new_button_frame, text="K", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('k',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=0, column=10)

    button = Button(new_button_frame, text="L", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('l',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=0, column=11)

    button = Button(new_button_frame, text="M", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('m',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=0, column=12)

    button = Button(new_button_frame, text="N", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('n',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=1, column=0)

    button = Button(new_button_frame, text="O", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('o',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=1, column=1)

    button = Button(new_button_frame, text="P", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('p',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=1, column=2)

    button = Button(new_button_frame, text="Q", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('q',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=1, column=3)

    button = Button(new_button_frame, text="R", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('r',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=1, column=4)

    button = Button(new_button_frame, text="S", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('s',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=1, column=5)

    button = Button(new_button_frame, text="T", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('t',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=1, column=6)

    button = Button(new_button_frame, text="U", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('u',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=1, column=7)

    button = Button(new_button_frame, text="V", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('v',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=1, column=8)

    button = Button(new_button_frame, text="W", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('w',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=1, column=9)

    button = Button(new_button_frame, text="X", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('x',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=1, column=10)

    button = Button(new_button_frame, text="Y", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('y',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=1, column=11)

    button = Button(new_button_frame, text="Z", font=('Arial', 10),padx=3,height=1,width=2,command=lambda :character('z',word,word_user_solution,tries_label,word_label,win),bg="DodgerBlue",fg="black")
    button.grid(row=1, column=12)


def open_window_name(words,players,tries):
    win_name=Toplevel(window)
    win_name.title("Enter name")
    win_name.geometry("450x450")
    win_name.configure(bg="gray70")

    name_label=Label(win_name,text="Player name: ",font=('Arial',11),bg="gray70",fg="black",highlightbackground="gray70")
    name_label.pack(pady=5)

    name_entry=Entry(win_name,validatecommand=lambda : checking_methods.username_exists(name_entry.get(),players,name_status),font=('Arial',11),bg="gray70",fg="black")
    name_entry.pack(pady=10)

    name_status=Label(win_name,text="Still waiting...",font=('Arial',11),fg="Red",bg="gray70")
    name_status.pack(pady=15)

    validate_button=Button(win_name,text="Validate name",font=('Arial',13),command=lambda : checking_methods.validate_name(name_entry.get(),players,name_status,game_button),bg="gray70")
    validate_button.pack(pady=45)

    game_button=Button(win_name,text="Play game",font=('Arial',13),state='disabled',command=lambda : open_window(words,players,tries,win_name,name_entry.get()),bg="gray70")
    game_button.pack()

def open_window(words,players,tries,win_name,new_player_name):
    players.append(new_player_name)
    win_name.destroy()

    index=random.randint(0, len(words) - 1)
    word=words[index]
    word_user_solution=["_  "]*len(word)
    result=""
    for c in word_user_solution:
        result=result+c

    win=Toplevel(window)
    win.title("Hangman")
    win.geometry("450x450")
    win.configure(bg="gray70")

    new_frame=Frame(win)
    word_label_title=Label(win,text="Guess word...",font=('Arial',15),bg="gray70")
    word_label_title.pack()
    new_frame.pack(padx=1,pady=1)

    frame_word=Frame(win)
    word_label=Label(win,font=('Arial',13),bg="gray70")
    word_label.configure(text=result)
    word_label.pack(padx=100,pady=100)
    frame_word.pack()

    frame_tries=Frame(win)
    tries_label=Label(win,text=f"Tries left: {tries}",font=('Arial',10),bg="gray70")
    tries_label.pack(pady=10)
    frame_tries.pack()

    new_button_frame=Frame(win)
    create_buttons(win,new_button_frame,word,word_user_solution,tries_label,word_label)
    new_button_frame.pack()


frame_button=Frame(window,bg="gray70")
button_start_game=Button(frame_button,text="Start game",font=('Arial',15),command=lambda: open_window_name(words,players,tries),bg="gray70",fg="black")
button_start_game.pack(pady=100)

button_quit_game=Button(frame_button,text="Quit game",font=('Arial',15),command=lambda : unpacking_methods.add_new_users(players,file_name_players,window),bg="gray70",fg="black")
button_quit_game.pack()

frame_button.pack(padx=10,pady=10)

if __name__=='__main__':
    file_name_words = "words.txt"
    file_name_players = "existing_users.txt"
    players = unpacking_methods.unpack_users(file_name_players)
    words = unpacking_methods.unpack_words(file_name_words)
    tries = 6
    window.mainloop()