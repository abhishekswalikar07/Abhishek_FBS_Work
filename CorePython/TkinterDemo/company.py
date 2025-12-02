from tkinter import *

from tkinter import messagebox

def clearScreen():
    for widget in window.winfo_children():
        widget.destroy()

def empManage():
    def loadData():
        with open ('CorePython/TkinterDemo/empDetails.txt','r') as fp:
            for row in fp:
                mylist.insert(END,row)

    def clearData():
        id_entry.delete(0,END)
        nm_entry.delete(0,END)
        sal_entry.delete(0,END)
        id_entry.focus()
    
    def addEmp():
        id=id_entry.get()
        nm=nm_entry.get()
        sal=sal_entry.get()
        eData=f'{id}, {nm}, {sal}'
        mylist.insert(END,eData)

        with open ('CorePython/TkinterDemo/empDetails.txt','a') as fp:
            fp.write(eData+'\n')
        clearData()
    
    def selEmp():
        clearData()
        eData=mylist.get(ACTIVE)
        # print(eData)
        eList=eData.split(', ')
        # print(eList)
        id_entry.insert(0,eList[0])
        nm_entry.insert(0,eList[1])
        sal_entry.insert(0,eList[2])

    def updEmp():
        pass
    def delEmp():
        id=id_entry.get()
        all_emp_list=[]
        with open ('CorePython/TkinterDemo/empDetails.txt','r') as fp:
            for row in fp:
                eList=row.split(', ')
                if id!=eList[0]:
                    all_emp_list.append(row)


    clearScreen()

    frame1=Frame(window)
    frame2=Frame(window)
    frame3=Frame(window)

    id_label=Label(frame1,text='ID:')
    id_entry=Entry(frame1)

    nm_label=Label(frame1,text='NAME:')
    nm_entry=Entry(frame1)

    sal_label=Label(frame1,text='SALARY:')
    sal_entry=Entry(frame1)

    id_label.grid(row=1,column=1)
    id_entry.grid(row=1,column=2)
    nm_label.grid(row=2,column=1)
    nm_entry.grid(row=2,column=2)
    sal_label.grid(row=3,column=1)
    sal_entry.grid(row=3,column=2)
    frame1.pack()

    add_btn=Button(frame2,text='ADD',command=addEmp)
    sel_btn=Button(frame2,text='SELECT',command=selEmp)
    upd_btn=Button(frame2,text='UPDATE',command=updEmp)
    del_btn=Button(frame2,text='DELETE',command=delEmp)
    add_btn.pack(side=LEFT)
    sel_btn.pack(side=LEFT)
    upd_btn.pack(side=LEFT)
    del_btn.pack(side=LEFT)
    frame2.pack()

    scrollbar=Scrollbar(frame3)
    scrollbar.pack(side=RIGHT,fill=Y)
    mylist=Listbox(frame3,yscrollcommand=scrollbar.set,height=15,width=40)
    mylist.pack(side=LEFT,fill=BOTH)
    scrollbar.config(command=mylist.yview)
    frame3.pack()

    loadData()


def login():
    uid=uid_entry.get()
    passw=passw_entry.get()
    if uid=='Admin' and passw=='1234':
        empManage()
    else:
        messagebox.showerror('Message',message='Invalid credentials..')


def main():
    user_id_label=Label(window,text='USERID:', pady=10)
    global uid_entry
    uid_entry=Entry(window)
    passw_label=Label(window,text='PASSWORD:',pady=10)
    global passw_entry
    passw_entry=Entry(window)
    btn=Button(window,text='LOGIN',command=login,pady=10)
    user_id_label.pack()
    uid_entry.pack()
    passw_label.pack()
    passw_entry.pack()
    btn.pack()

if __name__=='__main__':
    window=Tk()

    window.title("FBS")
    window.geometry('300x400')
    window.config(background='black')
    

    main()
    # empManage()

    window.mainloop()