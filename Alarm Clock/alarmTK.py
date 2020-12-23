from tkinter import *
from tkinter import messagebox
import datetime, time            # just import
from playsound import playsound  # pip install playsound

# change color of button when cursor on it
def button_hover(event):
    confirm["bg"] = "lightblue"

# change color of button when remove cursor from it
def button_hover_leave(event):
    confirm["bg"] = "SystemButtonFace"

# check time with alarm time, and turn ON alarm
def alarm(set_alarm):
    while True:
        current = datetime.datetime.now()

        date = current.strftime("%d.%m.%Y")
        time_atm = current.strftime("%H:%M:%S")

        if time_atm == set_alarm:
            print("Alarmaaaa")
        # in my case .mp3 file is in same folder
        playsound("Happy_Home.mp3")
        break

# recive data from user(spinbox)
def alarm_time():
    h = hour.get()
    m = minutes.get()

    answer = messagebox.showinfo("Set alarm",
        f"Alarm will signal at\n{h}:{m}")

    set_alarm = f"{h}:{m}:00"
    alarm(set_alarm)

if __name__ == "__main__":

    window = Tk()
    window.geometry("400x210")
    window.title("Alarm")

    choose_time = Label(text="Choose the alarm time")
    choose_time.place(x=20, y=20)
    
    hour = IntVar()
    Spinbox(width=4, from_=0, to=23, state="readonly", textvariable=hour,
            wrap=True).place(x=200, y=20)

    minutes = IntVar()
    Spinbox(width=4, from_=0, to=59, state="readonly", textvariable=minutes,
            wrap=True).place(x=240, y=20)

    confirm = Button(text="Set alarm", command=alarm_time, width=10, height=3)
    confirm.place(x=160, y=70)
    confirm.bind("<Enter>", button_hover)
    confirm.bind("<Leave>", button_hover_leave)

    exit = Button(text="Quit",width=10, command=window.destroy)
    exit.place(x=20, y=170)

    made_by = Label(text="made by @python3_fun").place(x = 260, y = 178)

    window.mainloop()