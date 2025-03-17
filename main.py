from tkinter import *

reset_timer = False
pause_timer = False
invalid_time = False

def remove():
    global reset_timer, pause_timer
    if reset_timer == False:
        start_button.grid_remove()
        time_entry_hours.grid_remove()
        time_entry_minutes.grid_remove()
        time_entry_seconds.grid_remove()
        time_label_hours.grid_remove()
        time_label_minutes.grid_remove()
        time_label_seconds.grid_remove()
    elif reset_timer == True:
        pause_button.grid_remove()
        reset_button.grid_remove()
        resume_button.grid_remove()
    
    if pause_timer == False and reset_timer == False:
        resume_button.grid_remove()
    elif pause_timer == True and reset_timer == False:
        pause_button.grid_remove()

def display():
    global reset_timer, pause_timer
    if reset_timer == False:
        pause_button.grid(column=0, row=0)
        reset_button.grid(column=1, row=0)
    elif reset_timer == True:
        start_button.grid(column=1, row=0)
        time_entry_hours.grid(column=0, row=1)
        time_entry_minutes.grid(column=0, row=2)
        time_entry_seconds.grid(column=0, row=3)
        time_label_hours.grid(column=1, row=1)
        time_label_minutes.grid(column=1, row=2)
        time_label_seconds.grid(column=1, row=3)
    
    if pause_timer == False and reset_timer == False:
        pause_button.grid(column=0, row=0)
    elif pause_timer == True and reset_timer == False:
        resume_button.grid(column=0, row=0)

def start_time():
    global reset_timer, pause_timer, invalid_time, time_in_seconds, time_hours, time_minutes, time_seconds
    reset_timer = False
    pause_timer = False
    invalid_time = False
    
    time_hours = int(time_entry_hours.get())
    time_minutes = int(time_entry_minutes.get())
    time_seconds = int(time_entry_seconds.get())
    if time_hours > 99:
        invalid_time = True
        error_label.config(text="Hours must be less than 100")
        raise ValueError("Hours must be less than 100")
    if time_minutes > 59:
        invalid_time = True
        error_label.config(text="Minutes must be less than 60")
        raise ValueError("Minutes must be less than 60")
    if time_seconds > 59:
        invalid_time = True
        error_label.config(text="Seconds must be less than 60")
        raise ValueError("Seconds must be less than 60")

    if invalid_time == False:
        remove()
        display()
        error_label.config(text="")
        time_in_seconds = time_hours * 3600 + time_minutes * 60 + time_seconds
        if time_hours < 10:
            time_hours = f"0{time_hours}"
        if time_minutes < 10:
            time_minutes = f"0{time_minutes}"
        if time_seconds < 10:
            time_seconds = f"0{time_seconds}"
        time_text.config(text=f"{time_hours}:{time_minutes}:{time_seconds}")
        countdown()

def countdown():
    global time_in_seconds, time_hours, time_minutes, time_seconds

    error_label.config(text="")
    if time_in_seconds > 0 and reset_timer == False and pause_timer == False:
        time_in_seconds -= 1
        time_hours = time_in_seconds // 3600
        time_minutes = (time_in_seconds % 3600) // 60
        time_seconds = time_in_seconds % 60
        if time_hours < 10:
            time_hours = f"0{time_hours}"
        if time_minutes < 10:
            time_minutes = f"0{time_minutes}"
        if time_seconds < 10:
            time_seconds = f"0{time_seconds}"
        time_text.config(text=f"{time_hours}:{time_minutes}:{time_seconds}")
        time_text.after(1000, countdown)
    elif reset_timer == True:
        return
    elif pause_timer == True:
        time_text.config(text=f"{time_hours}:{time_minutes}:{time_seconds}")
    else:
        time_text.config(text="Time's Up!")

def pause_time():
    global pause_timer
    pause_timer = True
    remove()
    display()

def resume_time():
    global pause_timer
    pause_timer = False
    remove()
    display()
    countdown()

def reset():
    global reset_timer, pause_timer, time_in_seconds, time_hours, time_minutes, time_seconds
    reset_timer = True
    pause_timer = False
    time_in_seconds = 0
    time_hours = 0
    time_minutes = 0
    time_seconds = 0
    time_text.config(text="00:00:00")
    remove()
    display()

root = Tk()
root.title("Countdown Timer")
root.geometry("400x200")

time_hours = 0
time_minutes = 0
time_seconds = 0
if time_hours < 10:
    time_hours = f"0{time_hours}"
if time_minutes < 10:
    time_minutes = f"0{time_minutes}"
if time_seconds < 10:
    time_seconds = f"0{time_seconds}"
time_text = Label(root, text=f"{time_hours}:{time_minutes}:{time_seconds}")
time_text.grid()

time_label_hours = Label(root, text="Hours")
time_label_hours.grid(column=1, row=1)
time_label_minutes = Label(root, text="Minutes")
time_label_minutes.grid(column=1, row=2)
time_label_seconds = Label(root, text="Seconds")
time_label_seconds.grid(column=1, row=3)
time_entry_hours = Entry(root)
time_entry_hours.grid(column=0, row=1)
time_entry_minutes = Entry(root)
time_entry_minutes.grid(column=0, row=2)
time_entry_seconds = Entry(root)
time_entry_seconds.grid(column=0, row=3)

button_frame = Frame(root)
button_frame.grid(column=0, row=4)

time_in_seconds = time_hours * 3600 + time_minutes * 60 + time_seconds
    
start_button = Button(button_frame, text="Start", command=start_time)
pause_button = Button(button_frame, text="Pause", command=pause_time)
reset_button = Button(button_frame, text="Reset", command=reset)
resume_button = Button(button_frame, text="Resume", command=resume_time)
pause_button.display = False
reset_button.display = False
resume_button.display = False

error_label = Label(root, text="", fg="red")
error_label.grid(column=0, row=5)

start_button.grid(column=1, row=0)

root.mainloop()