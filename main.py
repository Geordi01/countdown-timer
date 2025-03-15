from tkinter import *



reset_timer = False

def remove():
    global reset_timer
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

def display():
    global reset_timer
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

def start_time():
    global reset_timer, time_in_seconds, time_hours, time_minutes, time_seconds
    reset_timer = False
    remove()
    display()
    time_hours = int(time_entry_hours.get())
    time_minutes = int(time_entry_minutes.get())
    time_seconds = int(time_entry_seconds.get())
    time_in_seconds = time_hours * 3600 + time_minutes * 60 + time_seconds
    if time_hours < 10:
        time_hours = f"0{time_hours}"
    if time_minutes < 10:
        time_minutes = f"0{time_minutes}"
    if time_seconds < 10:
        time_seconds = f"0{time_seconds}"
    time_text.config(text=f"{time_hours}:{time_minutes}:{time_seconds}")
    countdown()

def pause_time():
    pass

def countdown():
    global time_in_seconds, time_hours, time_minutes, time_seconds

    if time_in_seconds > 0 and reset_timer == False:
        time_in_seconds -= 1
        time_hours = time_in_seconds // 3600
        time_minutes = (time_in_seconds // 60) - 60
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
    else:
        time_text.config(text="Time's Up!")

def reset():
    global reset_timer, time_in_seconds, time_hours, time_minutes, time_seconds
    reset_timer = True
    time_in_seconds = 0
    time_hours = 0
    time_minutes = 0
    time_seconds = 0
    time_text.config(text="00:00")
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
pause_button = Button(button_frame, text="Pause")
reset_button = Button(button_frame, text="Reset", command=reset)
pause_button.display = False
reset_button.display = False

start_button.grid(column=1, row=0)

root.mainloop()