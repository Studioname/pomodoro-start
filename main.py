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
check_mark = 0
check = "✓"
running = False
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global check_mark
    global reps
    global running
    check_mark = 0
    reps = 0
    running = False
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_string.config(text=check * check_mark)
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global running
    global reps
    global check_mark
    global started
    reps +=1
    if running == False:
        running = True
        if reps % 2 != 0:
            timer = WORK_MIN * 60
            timer_label.config(text="Work",fg=GREEN)
            window.bell()
        elif reps < 8:
            timer = SHORT_BREAK_MIN * 60
            timer_label.config(text="Short break", fg=PINK)
            check_mark += 1
            check_mark_string.config(text=check * check_mark)
            window.bell()
        else:
            timer = LONG_BREAK_MIN * 60
            timer_label.config(text="Long break", fg=RED)
            check_mark += 1
            check_mark_string.config(text=check * check_mark)
            window.bell()
    #if reps 1/3/5/7 work_min
    #if reps 2/4/6 short_break_min
    #else long_break_min
        count_down(timer)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    if running == True:
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = (f"0{count_sec}")
        # countdown_minutes : countdown_seconds
        canvas.itemconfig(timer_text,text=f"{count_min}" + ':' + f"{count_sec}")
        print(count)
        global timer
        if count > 0:
            timer = window.after(1000,count_down, count -1)
        else:
            start_timer()
    else:
        pass

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50,bg=YELLOW)
canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)



window.title("Pomodoro")
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(100,126, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 34, "normal"),bg=YELLOW,fg=GREEN)
timer_label.grid(column=1,row=0)

start_button = Button(text="Start",width=8,command=start_timer)
start_button.grid(column=0, row=2)


restart_button = Button(text = "Restart", width=8, command = reset_timer)
restart_button.grid(column=2,row=2)


check_mark_string = Label(text=check *check_mark, fg=GREEN,bg=YELLOW, font=("Arial", 18, "normal"))
check_mark_string.grid(column=1, row=2)


#timer 1,0
#start 0,2
#reset 2,2


window.mainloop()

#use fg keyword argument to colour a label ✓