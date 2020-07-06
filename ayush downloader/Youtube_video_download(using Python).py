import youtube_dl
from pytube import YouTube
import tkinter as tk
import os
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *

file_size=0
opts = {'outtmpl':'./videos/%(title)s.%(ext)s',}

def startDownload(x):
    global file_size
    try:
     with youtube_dl.YoutubeDL(opts) as y:
        PATH=filedialog.askdirectory()
        dBtn["state"]= tk.DISABLED
        dBtn["text"]='Just few minutes!!!'
        os.chdir(PATH)
        t = y.download([x])
        dBtn["state"]= tk.NORMAL
        dBtn["text"]='Download Again'
        

    except Exception as e:

         print(e)
         print("Sorry some error occur...") 


def ytl():
    v = url.get()
    url.delete(0,"end")
    if len(v) !=0:
        startDownload(v)
    else:
        print("error")
        

def clear():
    url.delete(first=0, last=100000000)
    




main=Tk()

main.title("My youtube downloader")


main.iconbitmap('i1.ico')

main.geometry("1000x600")

file=PhotoImage(file='i1.png')
headingIcon=Label(main,image=file)
headingIcon.pack(side=TOP)


url=Entry(main,font=("verdana",18),justify=CENTER)
url.pack(side=TOP,fill=X,padx=10)


dBtn =tk.Button(main,text="start download",font=("verdana",18),relief='ridge',command=ytl)
dBtn.pack(side=TOP)

clearButton = tk.Button(main, text="Clear",command=clear,fg="Black"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.pack(padx=5,pady=5)


m = tk.Label(main, text="Made By AYUSH", bg="aqua", fg="black", width=20,height=2, font=('times', 15, 'italic bold '))
m.pack(padx=5,pady=5)

button_quit =tk.Button(main,text="Exit",font=("verdana",20),relief='ridge',command=main.quit,fg="Black"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" )
button_quit.pack(padx=5,pady=5)



main.mainloop()



