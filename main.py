from tkinter import *

root = Tk()
root.title("Countdown Timer")
root.geometry("400x200")

time_minutes = 0
time_seconds = 0
if time_minutes < 10:
    time_minutes = f"0{time_minutes}"
if time_seconds < 10:
    time_seconds = f"0{time_seconds}"
time_text = Label(root, text=f"{time_minutes}:{time_seconds}")
time_text.grid()

time_label_minutes = Label(root, text="Minutes")
time_label_minutes.grid(column=1, row=1)
time_label_seconds = Label(root, text="Seconds")
time_label_seconds.grid(column=1, row=2)
time_entry_minutes = Entry(root)
time_entry_minutes.grid(column=0, row=1)
time_entry_seconds = Entry(root)

time_entry_seconds.grid(column=0, row=2)

button_frame = Frame(root)
button_frame.grid(column=0, row=3)

time_in_seconds = time_minutes * 60 + time_seconds

def set_time():
    global time_in_seconds, time_minutes, time_seconds
    time_minutes = int(time_entry_minutes.get())
    time_seconds = int(time_entry_seconds.get())
    time_in_seconds = time_minutes * 60 + time_seconds
    if time_minutes < 10:
        time_minutes = f"0{time_minutes}"
    if time_seconds < 10:
        time_seconds = f"0{time_seconds}"
    time_text.config(text=f"{time_minutes}:{time_seconds}")

def start_time():
    pause_button = Button(button_frame, text="Pause")
    reset_button = Button(button_frame, text="Reset")
    pause_button.grid(column=0, row=0)
    reset_button.grid(column=1, row=0)
    set_time_button.visible = False
    start_button.visible = False
    countdown()

def pause_time():
    pass

def countdown():
    global time_in_seconds, time_minutes, time_seconds
    #print(time_in_seconds, time_minutes, time_seconds)

    if time_in_seconds > 0:
        time_in_seconds -= 1
        time_minutes = time_in_seconds // 60
        time_seconds = time_in_seconds % 60
        if time_minutes < 10:
            time_minutes = f"0{time_minutes}"
        if time_seconds < 10:
            time_seconds = f"0{time_seconds}"
        time_text.config(text=f"{time_minutes}:{time_seconds}")
        time_text.after(1000, countdown)
    else:
        time_text.config(text="Time's Up!")

    
    



set_time_button = Button(button_frame, text="Set Time", command=set_time)
start_button = Button(button_frame, text="Start", command=start_time)

set_time_button.grid(column=0, row=0)
start_button.grid(column=1, row=0)







root.mainloop()