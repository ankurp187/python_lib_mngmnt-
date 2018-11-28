import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import pymysql
import pymysql.cursors


def f1(a,b):
    conn = pymysql.connect(host='localhost',user='root')
    a=conn.cursor()
    a.execute('use books')
    a.execute('select * from admins')
    data = a.fetchall()
    print(a)
    print(b)
    print(data)
    for i in range(len(data)):
        if(a==data[i][2] and b==data[i][1]):
            messagebox.showinfo("Welcome","Successfully signed in!")
        else:
            messagebox.showwarning("Warning","Authentication failed!")

root =Tk()
root.geometry('950x700+50+50')
label = Label(root,text="Login to library management system")
label.config(font=("Arial",27,"italic"))
label.place(x='200',y='100')

u = ttk.Label(root,text='user_id')
u.config(font=("Arial",27,"italic"))
u.place(x='200',y='300')
eu = ttk.Entry(root,width=40)
eu.place(x='400',y='300')

p = ttk.Label(root,text='password')
p.config(font=("Arial",27,"italic"))
p.place(x='200',y='400')
ep = ttk.Entry(root,width=40)
ep.place(x='400',y='400')

login = ttk.Button(root,text="LOGIN",width=30,command=lambda:f1(eu.get(),ep.get()))
login.place(x='650',y='500')



















'''
root = Tk()
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
mylist = Listbox(root,yscrollcommand=scrollbar.set)
for line in range(100):
    mylist.insert(END,"This is line number"+str(line))
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()

def f3():
    global a
    def f1():
        global a
        print(a)
    def f2():
        global a
        a=input("Enter ",)
        f1()
    f2()
f3()
'''
