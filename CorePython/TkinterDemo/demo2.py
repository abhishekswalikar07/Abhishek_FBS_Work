from tkinter import *

if (__name__=='__main__'):
    windows=Tk()
    windows.geometry('300x400')
    label=Label(windows,text="Hello world",background="aqua")
    label.pack()
    windows.mainloop()