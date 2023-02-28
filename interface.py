from tkinter import *
from PIL import ImageTk,Image

window=Tk()
window.title("Hangman")
window.geometry("400x400")
window.resizable(0,0)

frame_title=Frame(window)
label_title=Label(frame_title,text="The Hangman",justify=LEFT,font=('Arial',25))
label_title.pack(side=LEFT)
frame_title.pack(padx=1,pady=1)

def create_buttons(new_button_frame):
    button = Button(new_button_frame, text="A", font=('Arial', 10),padx=5)
    button.grid(row=0, column=0)

    button = Button(new_button_frame, text="B", font=('Arial', 10),padx=5)
    button.grid(row=0, column=1)

    button = Button(new_button_frame, text="C", font=('Arial', 10),padx=5)
    button.grid(row=0, column=2)

    button = Button(new_button_frame, text="D", font=('Arial', 10),padx=5)
    button.grid(row=0, column=3)

    button = Button(new_button_frame, text="E", font=('Arial', 10),padx=5)
    button.grid(row=0, column=4)

    button = Button(new_button_frame, text="F", font=('Arial', 10),padx=5)
    button.grid(row=0, column=5)

    button = Button(new_button_frame, text="G", font=('Arial', 10),padx=5)
    button.grid(row=0, column=6)

    button = Button(new_button_frame, text="H", font=('Arial', 10),padx=5)
    button.grid(row=0, column=7)

    button = Button(new_button_frame, text="I", font=('Arial', 10),padx=5)
    button.grid(row=0, column=8)

    button = Button(new_button_frame, text="J", font=('Arial', 10),padx=5)
    button.grid(row=0, column=9)

    button = Button(new_button_frame, text="K", font=('Arial', 10),padx=5)
    button.grid(row=0, column=10)

    button = Button(new_button_frame, text="L", font=('Arial', 10),padx=5)
    button.grid(row=0, column=11)

    button = Button(new_button_frame, text="M", font=('Arial', 10),padx=5)
    button.grid(row=0, column=12)

    button = Button(new_button_frame, text="N", font=('Arial', 10),padx=5)
    button.grid(row=1, column=0)

    button = Button(new_button_frame, text="O", font=('Arial', 10),padx=5)
    button.grid(row=1, column=1)

    button = Button(new_button_frame, text="P", font=('Arial', 10),padx=5)
    button.grid(row=1, column=2)

    button = Button(new_button_frame, text="Q", font=('Arial', 10),padx=5)
    button.grid(row=1, column=3)

    button = Button(new_button_frame, text="R", font=('Arial', 10),padx=5)
    button.grid(row=1, column=4)

    button = Button(new_button_frame, text="S", font=('Arial', 10),padx=5)
    button.grid(row=1, column=5)

    button = Button(new_button_frame, text="T", font=('Arial', 10),padx=5)
    button.grid(row=1, column=6)

    button = Button(new_button_frame, text="U", font=('Arial', 10),padx=5)
    button.grid(row=1, column=7)

    button = Button(new_button_frame, text="V", font=('Arial', 10),padx=5)
    button.grid(row=1, column=8)

    button = Button(new_button_frame, text="W", font=('Arial', 10),padx=5)
    button.grid(row=1, column=9)

    button = Button(new_button_frame, text="X", font=('Arial', 10),padx=5)
    button.grid(row=1, column=10)

    button = Button(new_button_frame, text="Y", font=('Arial', 10),padx=5)
    button.grid(row=1, column=11)

    button = Button(new_button_frame, text="Z", font=('Arial', 10),padx=5)
    button.grid(row=1, column=12)

def open_window():
    win=Toplevel(window)
    win.title("Hangman")
    win.geometry("400x400")

    new_frame=Frame(win)
    word_label_title=Label(win,text="Guess word...",font=('Arial',15))
    word_label_title.pack()
    new_frame.pack(padx=1,pady=1)

    frame_word=Frame(win)
    word_label=Label(win,text="_  _  _  _  _",font=('Arial',13))
    word_label.pack(padx=100,pady=100)
    frame_word.pack()

    frame_tries=Frame(win)
    tries_label=Label(win,text="Tries left: 6",font=('Arial',10))
    tries_label.pack(pady=10)
    frame_tries.pack()

    new_button_frame=Frame(win)
    create_buttons(new_button_frame)
    new_button_frame.pack()


frame_button=Frame(window)
button=Button(frame_button,text="Play game",font=('Arial',15),command=open_window)
button.pack(pady=100)
frame_button.pack(padx=10,pady=10)

window.mainloop()