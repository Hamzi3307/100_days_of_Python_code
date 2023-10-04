from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "green"
try:
    data = pd.read_csv("Day31\data\words_to_learn.csv")
except:
    data = pd.read_csv("Day31\data\\french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = to_learn[random.randint(0,len(to_learn))]
    WORD = current_card["French"]
    canvas.itemconfig(word_text,text=WORD)
    canvas.itemconfig(title_text, text="French")
    flip_timer = window.after(3000,flip_card)

def flip_card():
    WORD = current_card["English"]
    flip_img = PhotoImage(file="Day31\images\card_back.png")
    canvas.itemconfig(image_card, image=flip_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=WORD, fill="white")

def is_known():
    global to_learn
    to_learn.remove(current_card)
    list_data = pd.DataFrame(to_learn)
    list_data.to_csv("Day31\data\words_to_learn.csv")
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,flip_card)


canvas = Canvas(width=800, height=526)
img = PhotoImage(file="Day31\images\card_front.png")
image_card = canvas.create_image(408, 268, image=img)
title_text = canvas.create_text(388, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(388, 268, text="", font=("Arial", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

next_card()

cross = PhotoImage(file="Day31\images\wrong.png")
unknown_button = Button(image=cross, command=next_card)
unknown_button.grid(row=1, column=0)

tick = PhotoImage(file="Day31\images\\right.png")
known_button = Button(image=tick, command=is_known)
known_button.grid(row=1, column=1)

window.mainloop()