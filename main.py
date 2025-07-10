from tkinter import *
import math
# pip install pyttsx3
import pyttsx3

speak = pyttsx3.init()

work_text = "start working"
break_text = "take a break for 5 minutes"
long_break_text = "take a break you have 20 minutes ( coffee time )"

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    ws = WORK_MIN * 60
    sb = SHORT_BREAK_MIN * 60
    lb = LONG_BREAK_MIN * 60
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(lb)
        title_label.config(text="Break", fg=RED)
        speak.say(long_break_text)
    elif reps % 2 == 0:
        count_down(sb)
        title_label.config(text="Break", fg=PINK)
        speak.say(break_text)
    else:
        count_down(ws)
        title_label.config(text="Work", fg=GREEN)
        speak.say(work_text)
    speak.runAndWait()
    speak.stop()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    m = int(count / 60)
    s = count % 60

    if len(str(m)) == 1:
        m = f"0{m}"
    if len(str(s)) == 1:
        s = f"0{s}"

    canvas.itemconfig(timer_text, text=f"{m}:{s}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(int(reps / 2)):
            marks += "✔"
            check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
