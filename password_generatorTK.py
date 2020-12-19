from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import string
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation

def button_hover(event):
    generate["bg"] = "lightblue"

def button_hover_leave(event):
    generate["bg"] = "SystemButtonFace"

def generate():
    output.delete("1.0", END)
    choice = ""
    if choice_upper.get() == 1:
        choice = choice + upper
    if choice_lower.get() == 1:
        choice = choice + lower
    if choice_number.get() == 1:
        choice = choice + digits
    if choice_special.get() == 1:
        choice = choice + special

    level = len_scale.get()
    result = random.choices(choice, k=level)
    new_password = "".join(result)

    output.insert(END, new_password)
    print(new_password)

if __name__ == "__main__":

    window = Tk()
    window.geometry("400x240")
    window.title("Password Generator")

    len_password = Label(text="Choose length of password")
    len_password.place(x=20, y=20)
    
    len_scale = IntVar()        
    scale = ttk.Scale(orient=HORIZONTAL, length=80, from_=8, to=16,
                variable=len_scale)
    scale.place(x=252, y=20)

    choice_lbl = Label(text="Choose simbols of you password")
    choice_lbl.place(x=20, y=50)

    choice_upper = IntVar()
    choice1 = ttk.Checkbutton(text="Upper case", variable=choice_upper)
    choice1.place(x=250, y=50)

    choice_lower = IntVar()
    choice2 = ttk.Checkbutton(text="Lower case", variable=choice_lower)
    choice2.place(x=250, y=70)

    choice_number = IntVar()
    choice3 = ttk.Checkbutton(text="Numbers", variable=choice_number)
    choice3.place(x=250, y=90)

    choice_special = IntVar()
    choice4 = ttk.Checkbutton(text="Special symbols", variable=choice_special)
    choice4.place(x=250, y=110)

    generate = Button(text="Generate",width=10, command=generate)
    generate.place(x=20, y=150)
    generate.bind("<Enter>", button_hover)
    generate.bind("<Leave>", button_hover_leave)

    output = Text(height=1.4, width=30, bg="lightblue")
    output.place(x=130, y=155)

    exit = Button(text="Quit",width=10, command=window.destroy).place(x=20, y=200)

    made_by = Label(text="made by @python3_fun").place(x = 260, y = 208)

    window.mainloop()