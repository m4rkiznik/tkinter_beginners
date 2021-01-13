from tkinter import *
from tkinter import messagebox as mb
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd

class Window:
    def __init__(self, width, height, title="PY notebook", icon="logo.ico"):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.iconbitmap(icon)
        self.text = ScrolledText(self.root, padx=5, pady=5, wrap=WORD)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.draw_menu()
        self.text.place(relwidth=1, relheight=1)

    def draw_menu(self):
        menu_bar = Menu(self.root)

        # creating a file menu in menu_bar
        filemenu = Menu(menu_bar, tearoff=0)
        info_menu = Menu(menu_bar, tearoff=0)
        # creating the column in menu
        menu_bar.add_cascade(label="File", menu=filemenu)
        menu_bar.add_cascade(label="Info", menu=info_menu)

        info_menu.add_command(label="Contact", command=self.show_info)
        filemenu.add_command(label="New", command=self.new)
        filemenu.add_command(label="Open", command=self.openIt)
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit)
        self.root.configure(menu=menu_bar)

    def show_info(self):
        mb.showinfo("Contact",
            "Instagram: @python3_fun\nGitHub: github.com/m4rkiznik")

    def new(self):
        self.text.delete("1.0", END)

    def openIt(self):
        file = fd.askopenfilename(initialdir="C:/", title="Open file",
            filetypes=(("Text type", "*.txt"),
                       ("All types", "*.*"),
                       ("Python type", "*.py")))
        if file:
            with open(file, "r") as f:
                self.text.insert("1.0", f.read())

    def save(self):
        name = fd.asksaveasfilename(
            defaultextension="*.txt",
            filetypes=(("Text files", "*.txt"), ("Python files", "*.py")))
        text_doc = self.text.get("1.0", END)
        with open(name, "w") as f:
            f.write(text_doc)

    def exit(self):
        choice = mb.askyesno("Exit", "Do you want to quit?")
        if choice:
            self.root.destroy()    


if __name__ == "__main__":
    window = Window(500, 500)

    window.run()