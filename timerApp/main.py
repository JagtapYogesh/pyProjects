from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_counts():
    global reps
    reps = 1
    window.after_cancel(timer)
    checkmark_label.config(text="")
    do_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_countdown():
    if reps % 2 == 1:
        do_label.config(text="Work")
        start(WORK_MIN * 60)
    elif reps == 8:
        do_label.config(text="Long Break", fg=RED)
        checkmark_label.config(text="✔✔✔")
        start(LONG_BREAK_MIN * 60)
    else:
        do_label.config(text="Short Break", fg=PINK)
        if reps == 2:
            checkmark_label.config(text="✔")
        elif reps == 4:
            checkmark_label.config(text="✔✔")
        start(SHORT_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start(count):
    global timer
    min_time = math.floor(count/60)
    sec_time = count % 60
    if sec_time < 10:
        sec_time = f"0{sec_time}"
    canvas.itemconfig(timer_text, text=f"{min_time}:{sec_time}")
    if count > 0:
        timer = window.after(1000, start, count-1)
    else:
        global reps
        reps += 1
        if reps <= 8:
            start_countdown()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

do_label = Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN)
canvas = Canvas(bg=YELLOW, height=224, width=200)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(100, 115, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
start_button = Button(text="Start", bg=YELLOW, command=start_countdown)
reset_button = Button(text="Reset", bg=YELLOW, command=reset_counts)
checkmark_label = Label(text="", fg=GREEN, font=(FONT_NAME, 15, "bold"))

do_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
checkmark_label.grid(row=5, column=1)



window.mainloop()