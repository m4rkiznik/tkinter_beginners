from tkinter import *

window = Tk()
window.title("Calculator")

# allows multiple input, and 
# setting the nText
def add(text):
    txt = nText.get()
    if txt == "Error":
        nText.set("Error")
    else:
        nText.set(txt + text)

def reset():
    nText.set("")

def delete():
    nText.set(nText.get()[:-1])

def calc():
    try:
        nText.set(eval(nText.get()))
    except:
        nText.set("Error")

nText = StringVar()
Entry(window, textvariable = nText, font = ("Times 18")).grid(sticky = NW, column = 0, columnspan = 4)

Button(window, text = "C", command = reset, font = ("Times 18"), width = 4).grid(row = 1, column = 0)
Button(window, text = "<", command = delete, font = ("Times 18"), width = 4).grid(row = 1, column = 1)
Button(window, text = "/", command = lambda:add("/"), font = ("Times 18"), width = 4).grid(row = 1, column = 2)
Button(window, text = "*", command = lambda:add("*"), font = ("Times 18"), width = 4).grid(row = 1, column = 3)

Button(window, text = "7", command = lambda:add("7"), font = ("Times 18"), width = 4).grid(row = 2, column = 0)
Button(window, text = "8", command = lambda:add("8"), font = ("Times 18"), width = 4).grid(row = 2, column = 1)
Button(window, text = "9", command = lambda:add("9"), font = ("Times 18"), width = 4).grid(row = 2, column = 2)
Button(window, text = "+", command = lambda:add("+"), font = ("Times 18"), width = 4).grid(row = 2, column = 3)

Button(window, text = "4", command = lambda:add("4"), font = ("Times 18"), width = 4).grid(row = 3, column = 0)
Button(window, text = "5", command = lambda:add("5"), font = ("Times 18"), width = 4).grid(row = 3, column = 1)
Button(window, text = "6", command = lambda:add("6"), font = ("Times 18"), width = 4).grid(row = 3, column = 2)
Button(window, text = "-", command = lambda:add("-"), font = ("Times 18"), width = 4).grid(row = 3, column = 3)

Button(window, text = "1", command = lambda:add("1"), font = ("Times 18"), width = 4).grid(row = 4, column = 0)
Button(window, text = "2", command = lambda:add("2"), font = ("Times 18"), width = 4).grid(row = 4, column = 1)
Button(window, text = "3", command = lambda:add("3"), font = ("Times 18"), width = 4).grid(row = 4, column = 2)
Button(window, text = "=", command = calc, font = ("Times 18"), width = 4).grid(sticky = NS, row = 4, column = 3, rowspan = 2)

Button(window, text = "0", command = lambda:add("0"), font = ("Times 18"), width = 4).grid(sticky = EW, row = 5, columnspan = 2)
Button(window, text = ".", command = lambda:add("."), font = ("Times 18"), width = 4).grid(row = 5, column = 2)

Label(window, text = "made by @python3_fun").grid(row = 6, columnspan = 4)

window.mainloop()