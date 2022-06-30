from tkinter import *
import math
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def timer_reset():
    # Play beep
    playsound("beep-07a.mp3")

    # Stop the counter
    global timer
    window.after_cancel(timer)

    # Reset the reps var
    global reps
    reps = 0

    # Reset the timer text
    canvas.itemconfig(timer_text, text="00:00")

    # Reset the title
    timer_label.config(text="Timer", foreground=GREEN)

    # Delete all ticks
    tick_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    WORK_SEC = WORK_MIN * 60
    SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
    LONG_BREAK_SEC = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Long break", foreground=RED)
        count_down(LONG_BREAK_SEC)
    elif reps % 2 == 0:
        timer_label.config(text="Short break", foreground=PINK)
        count_down(SHORT_BREAK_SEC)
    else:
        timer_label.config(text="Work", foreground=GREEN)
        count_down(WORK_SEC)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec in range(0, 10):
        count_sec = f"0{count_sec}"

    if count_min in range(0, 10):
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        playsound("beep-07a.mp3")
        mark = ""
        session = math.floor(reps / 2)

        for _ in range(session):
            mark += "✓"

        tick_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(101, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), foreground=GREEN, bg=YELLOW, justify="center")
timer_label.grid(column=1, row=0)

# Buttons
start_button = Button(text="Start")
start_button.config(font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset")
reset_button.config(font=(FONT_NAME, 10, "bold"), command=timer_reset)
reset_button.grid(column=2, row=2)

tick_label = Label(font=(FONT_NAME, 20, "bold"), foreground=GREEN, bg=YELLOW, justify="center")
tick_label.grid(column=1, row=3)

window.mainloop()
