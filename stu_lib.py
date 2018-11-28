import pymysql
import pymysql.cursors
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

def sea_stud_lib(sid):
    conn=pymysql.connect(host='localhost',user='root')
    a=conn.cursor()
    a.execute('use books')
    a.execute('create table if not exists s'+str(sid)+'(Book_code int,Book_name char(60),Author_name char(60),constraint primary key(Book_name,Author_name))')
    a.execute('select * from s'+str(sid))
    data=a.fetchall()
    if(len(data)==0):
        messagebox.showinfo("Book Inquiry","No Books Due")
    else:
        root1=Tk()
        root1.geometry("1300x700+100+75")
        for i in range(len(data)):
            for j in range(len(data[i])):
                label=ttk.Label(root1,text=data[i][j])
                label.place(x=str(150*(j+1)),y=str(50*(i+2)))
                label.config(font=('Helvetica',14,"bold") ,background = 'cyan',foreground = 'black')


def base_lib():
    root = Tk()
    root.geometry("400x250+600+300")
    root.config(background = 'cyan')
    root.title("Library Management System By Ankur Kumar Pandey")
    label = ttk.Label(root,text = "Enter Student Id To Get The Information")
    label.place(x='10',y='80')
    label.config(font=('Helvetica',14,"bold") ,background = 'cyan',foreground = 'black')
    s_id = ttk.Entry(root,width=20)
    s_id.place(x='50',y='170')
    submit = ttk.Button(root,text="Search",command=lambda:[sea_stud_lib(int(s_id.get())),root.destroy()])
    submit.place(x='250',y='170')
