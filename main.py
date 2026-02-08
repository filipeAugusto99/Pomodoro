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
reps = 0


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    print(reps)

    work_seg = WORK_MIN * 60
    short_break_seg = SHORT_BREAK_MIN * 60
    long_break_seg = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down(long_break_seg)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 != 0:
        count_down(work_seg)
        timer_label.config(text="Work", fg=GREEN)

    else:
        count_down(short_break_seg)
        timer_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_seg = count % 60


    if count_seg < 10:
        count_seg = f"0{count_seg}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seg}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create Timer Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

# Create Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

# Create Start Button
start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

#Create a Check Label

check_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=("normal", 15))
check_label.grid(column=1, row=3)

# Create Reset Button
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"))
reset_button.grid(column=2, row=2)



window.mainloop()