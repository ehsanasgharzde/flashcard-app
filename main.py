# ---------------------------- LIBRARIES ------------------------------- #
from tkinter import *
from random import choice
from tkinter import messagebox
import pandas


# ---------------------------- CONSTANTS ------------------------------- #
PURPLE = '#54436B'
LIGHTPURPLE = '#3E215D'
GREENBLUE = '#50CB93'
LIGHTGREEN = '#71EFA3'
LIGHT = '#ACFFAD'
FLIPTIME = None
TOLEARN = {}
WORDBOX = {}

try:
    DATA = pandas.read_csv('Data/tolearnwords.csv')
except FileNotFoundError:
    ORGDATA = pandas.read_csv('Data/words.csv')
    TOLEARN = ORGDATA.to_dict(orient='records')
else:
    TOLEARN = DATA.to_dict(orient='records')

# ---------------------------- NEXT CARD SET ------------------------------- #
def nextcard():
    global WORDBOX, fliptimer

    window.after_cancel(fliptimer)

    WORDBOX = (choice(TOLEARN))
    french = WORDBOX['French']

    canvas.itemconfig(card, image=CARDFRONT)
    canvas.itemconfig(title, text='French', fill=GREENBLUE)
    canvas.itemconfig(word, text=french, fill=GREENBLUE)

    fliptimer = window.after(3000, func=flipcard)

# ---------------------------- CARD FLIPPER ------------------------------- #
def flipcard():
    global WORDBOX

    english = WORDBOX['English']
    canvas.itemconfig(card, image=CARDBACK)
    canvas.itemconfig(title, text='English', fill=LIGHT)
    canvas.itemconfig(word, text=english, fill=LIGHT)

# ---------------------------- CARD FLIPPER ------------------------------- #
def learnedcard():
    TOLEARN.remove(WORDBOX)
    pandas.DataFrame(TOLEARN).to_csv('Data/tolearnwords.csv', index=False)
    nextcard()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('French-Flash')
window.minsize(1000, 750)
window.config(bg=PURPLE)

fliptimer = window.after(3000, func=flipcard)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=PURPLE)
CARDFRONT = PhotoImage(file='Images/front.png')
CARDBACK = PhotoImage(file='Images/back.png')
card = canvas.create_image(400, 263, image=CARDFRONT)
title = canvas.create_text(400, 50, text='FRENCH', fill=GREENBLUE, font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 250, text='FRENCH', fill=GREENBLUE, font=('Arial', 60, 'bold'))
canvas.place(x=100, y=50)

CORRECTIMG = PhotoImage(file='Images/correct.png')
correctbutton = Button(image=CORRECTIMG, highlightthickness=0, bg=PURPLE, activebackground=PURPLE, border=0, command=learnedcard)
correctbutton.place(x=692, y=600)

WRONGIMG = PhotoImage(file='Images/wrong.png')
wrongbutton = Button(image=WRONGIMG, highlightthickness=0, bg=PURPLE, activebackground=PURPLE, border=0, command=nextcard)
wrongbutton.place(x=200, y=600)

nextcard()

window.mainloop()