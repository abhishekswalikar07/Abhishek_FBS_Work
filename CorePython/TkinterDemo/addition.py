from tkinter import *

def add():
    # print("In add funnction")
    num1=int(txt1.get())
    num2=int(txt2.get())
    sum=num1+num2

    oplabel.config(text='Addition:'+str(sum))

if __name__=='__main__':
    window=Tk()

    window.title("Addition")
    window.geometry('300x400')
    window.config(background='gray')

    label1=Label(window,text='Enter number 1:')
    txt1=Entry(window)

    label2=Label(window,text='Enter number 2:')
    txt2=Entry(window)
    btn=Button(window, text='ADDITION',command=add)
    oplabel=Label(window)

    label1.grid(row=1, column=1)
    txt1.grid(row=1, column=2)

    label2.grid(row=2,column=1)
    txt2.grid(row=2, column=2)

    btn.grid(row=3,column=1,columnspan=2)
    oplabel.grid(row=4,column=1,columnspan=2)

    window.mainloop()