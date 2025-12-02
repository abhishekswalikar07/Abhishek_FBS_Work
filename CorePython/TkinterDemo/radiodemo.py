from tkinter import *
from tkinter import messagebox

def changeTheme():
    val=x.get()

    if val==1:
        window.config(background='black')
    elif val==2:
        window.config(background='red')
    elif val==3:
        window.config(background='yellow')
    else:
        messagebox.showwarning("Warning",message="Please select color... ")

if __name__=='__main__':
    window=Tk()
    window.title("Theme Changing")
    window.geometry('300x400')
    window.config(background="gray")

    x=IntVar()
   

    label=Label(window,text="Please select background color:")
    rd01=Radiobutton(window,text='Black',variable=x,value=1)
    rd02=Radiobutton(window,text='Red',variable=x,value=2)
    rd03=Radiobutton(window,text='Yellow',variable=x,value=3)

    btn=Button(window,text='Change theme',command=changeTheme)
    label.grid(row=1,column=1)
    rd01.grid(row=2,column=1)
    rd02.grid(row=3,column=1)
    rd03.grid(row=4,column=1)
    btn.grid(row=5,column=1)
    window.mainloop()