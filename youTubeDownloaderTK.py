import os
from tkinter import filedialog
from tkinter import *
from pytube import YouTube

def file_dialog():
    # function to choose the directory
    # whare to save the file
    global browse
    browse = filedialog.askdirectory()

    lbl_browse = Label(text = "")
    lbl_browse.place(x = 20, y = 80)
    lbl_browse.configure(text = browse)

def download():
    # get input URL, creating a object and download video
    url = url_entry.get()
    yt = YouTube(url)

    stream = yt.streams.filter(progressive=True).first()

    stream.download(browse)

if __name__ == "__main__":

    window = Tk()
    window.geometry("400x240")
    window.title("YouTube downloader")

    url = Label(text="Put your URL addres of video: ")
    url.place(x=20, y=20)

    url_entry = Entry(width = 30)
    url_entry.place(x = 190, y = 20)

    save_file = Label(text="Choose direction whare want to save the video")
    save_file.place(x = 20, y = 50)

    browse_but = Button(text = "Browse", command = file_dialog)
    browse_but.place(x = 325, y = 45)

    download_but = Button(text = "Download", command = download)
    download_but.place(x = 309, y = 110)

    made_by = Label(text="made by @python3_fun").place(x = 260, y = 208)

    window.mainloop()