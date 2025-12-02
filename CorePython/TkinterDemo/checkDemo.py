from tkinter import *

from tkinter import messagebox

def submit():
    val1=x.get()
    val2=y.get()
    val3=z.get()
    data=''

    if val1==1:
        data+='Java\n'
    if val2==1:
        data+='Python\n'
    if val3==1:
        data+='Testing\n'
    
    if data:
        messagebox.showinfo(title='Courses',message=data)
    else:
        messagebox.showwarning(title='Warning', message='Please selecgt course...')

    

if __name__=='__main__':
    window=Tk()
    window.geometry('300x400')
    window.config(background="gray")

    x=IntVar()
    y=IntVar()
    z=IntVar()

    frame1=Frame(window)
    frame2=Frame(window)
    frame3=Frame(window)
    label=Label(frame1,text="Please select courses:")
    label.pack()
    frame1.pack()


    ch1=Checkbutton(frame2,text="Java", variable=x)
    ch2=Checkbutton(frame2,text="Python", variable=y)
    ch3=Checkbutton(frame2,text="Testing", variable=z)

    ch1.pack(side=LEFT)
    ch2.pack(side=LEFT)
    ch3.pack(side=LEFT)
    frame2.pack()

    btn=Button(frame3,text='Submit',command=submit)
    btn.pack()
    frame3.pack()


    window.mainloop()