from tkinter import *
import pandas
import random


def user_knows_answer():
    global GUESSED_INDEXES
    GUESSED_INDEXES.append(french_word_index)
    show_question()


def show_answer():
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(canvas_lang_text, text="english")
    canvas.itemconfig(canvas_word_text, text=data.English[french_word_index])


def show_question():
    window.after_cancel(flip)
    global french_word_index
    french_word_index = random.randint(0, 100)
    while french_word_index in GUESSED_INDEXES:
        french_word_index = random.randint(0, 100)
        if len(GUESSED_INDEXES) == 101:
            canvas.itemconfig(canvas_word_text, text="No more words available to learn")
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(canvas_lang_text, text="french")
    canvas.itemconfig(canvas_word_text, text=data.French[french_word_index])
    window.after(5000, show_answer)


BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 25, "italic")
WORD_FONT = ("Helvetica", 40, "bold")
GUESSED_INDEXES = []

data = pandas.read_csv("data/french_words.csv")

window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=10)
french_word_index = 0

flip = window.after(5000, show_answer)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_button_img = PhotoImage(file="images/right.png")
wrong_button_img = PhotoImage(file="images/wrong.png")

canvas = Canvas(window, highlightthickness=0, width=800, height=526, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263)
canvas_lang_text = canvas.create_text(400, 100, font=LANG_FONT)
canvas_word_text = canvas.create_text(400, 263, font=WORD_FONT)
right_button = Button(image=right_button_img, highlightthickness=0, command=user_knows_answer, borderwidth=0)
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=show_question, borderwidth=0)

canvas.grid(row=0, columnspan=2)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

show_question()

window.mainloop()
