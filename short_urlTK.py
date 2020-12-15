from tkinter import *
import pyshorteners as ps

# button change colour when coursor on it
def button_hover(event):
    button["bg"] = "lightblue"

# button defoult colour when coursor not on it
def button_hover_leave(event):
    button["bg"] = "SystemButtonFace"

# creating object, and URL convert to shortURL
def short():
    obj = ps.Shortener()
    url = url_entry.get()

    try:
        short_url = obj.tinyurl.short(url)
        output.insert(END, short_url)
    except:
        text = "Incorrect URL address"
        output.insert(END, text)

if __name__ == "__main__":

    window = Tk()
    window.geometry("400x240")
    window.title("URL shortener")

    url_lbl = Label(text="Put your URL address:")
    url_lbl.place(x=20, y=20)
    
    url_entry = Entry(width=35)
    url_entry.place(x=150, y=20)

    button = Button(text="Make sort URL", command=short, width=20)
    button.place(x=121, y=80)
    button.bind("<Enter>", button_hover)
    button.bind("<Leave>", button_hover_leave)

    output = Text(height=1.3, width=30, bg="lightblue")
    output.place(x=80, y=120)

    exit = Button(text="Quit",width=10, command=window.destroy)
    exit.place(x=20, y=200)

    made_by = Label(text="made by @python3_fun").place(x = 260, y = 208)

    window.mainloop()