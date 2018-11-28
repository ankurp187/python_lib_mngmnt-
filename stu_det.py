from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import database


def stud_fill():
    root = Tk()
    root.geometry("1100x750+75+50")
    root.config(background = 'cyan')
    root.title("Library Management System By Ankur Kumar Pandey")

    label = ttk.Label(root,text = "Student Details")
    label.place(x='450',y='100')
    label.config(font=('Helvetica',27,"bold") ,background = 'violet',foreground = 'red')
    #==============================================================================================
    lname = ttk.Label(root,text = " Student Name")
    lname.place(x='350',y='250')
    lname.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
    ename = ttk.Entry(root,width=40)
    ename.place(x='550',y='250')

    lfname = ttk.Label(root,text = " Father's Name")
    lfname.place(x='350',y='300')
    lfname.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
    efname = ttk.Entry(root,width=40)
    efname.place(x='550',y='300')

    lroll = ttk.Label(root,text = " Student Roll No")
    lroll.place(x='350',y='350')
    lroll.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
    eroll = ttk.Entry(root,width=40)
    eroll.place(x='550',y='350')

    lemail = ttk.Label(root,text = " Student Email")
    lemail.place(x='350',y='400')
    lemail.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
    eemail = ttk.Entry(root,width=40)
    eemail.place(x='550',y='400')

    lphn = ttk.Label(root,text = " Phone Number")
    lphn.place(x='350',y='450')
    lphn.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
    ephn = ttk.Entry(root,width=40)
    ephn.place(x='550',y='450')
    #==============================================================================================
    ladd = ttk.Label(root,text = " Address")
    ladd.place(x='350',y='500')
    ladd.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
    eadd = ttk.Entry(root,width=40)
    eadd.place(x='550',y='500')

    lcity = ttk.Label(root,text = " City")
    lcity.place(x='350',y='550')
    lcity.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
    ecity = ttk.Entry(root,width=40)
    ecity.place(x='550',y='550')
    #==============================================================================================
    submit = ttk.Button(root,text = 'Submit Details',width=20,command =lambda:database.stud_ent(ename.get(),efname.get(),eroll.get(),eemail.get(),ephn.get(),eadd.get(),ecity.get()))
    submit.place(x='480',y='650')
