from tkinter import *
from tkinter import ttk
from tkinter import font
import database

def book_en():
    global det,ename,eaname,eid,estr,esid,submit,search

    #==============================================================================================
    def func():
        global ename,eaname,eid,estr,esid,submit,search
        if det.get()=='search':
            ename.state(['disabled'])
            eaname.state(['disabled'])
            eid.state(['disabled'])
            estr.state(['disabled'])
            esid.state(['!disabled'])
            submit.state(['disabled'])
            search.state(['!disabled'])

        elif det.get()=='insert':
            ename.state(['!disabled'])
            eaname.state(['!disabled'])
            eid.state(['!disabled'])
            estr.state(['!disabled'])
            esid.state(['disabled'])
            submit.state(['!disabled'])
            search.state(['disabled'])

    #==============================================================================================

    def book_ent():
        global det,ename,eaname,eid,estr,esid,submit,search
        root = Tk()

        root.geometry("1100x750+75+50")
        root.config(background = 'cyan')
        root.title("Library Management System By Ankur Kumar Pandey")

        label = ttk.Label(root,text = "Book Entry")
        label.place(x='450',y='100')
        label.config(font=('Helvetica',27,"bold") ,background = 'violet',foreground = 'red')

        #==============================================================================================

        det=StringVar()
        sradiob = ttk.Radiobutton(root,text = 'Search by Book Id',variable = det,value='search')
        sradiob.place(x='350',y='250')

        iradiob = ttk.Radiobutton(root,text = 'Insert Book Details',variable = det,value='insert')
        iradiob.place(x='550',y='250')

        asubmit = ttk.Button(root,text = 'Choose the Action',width=20,command = func)
        asubmit.place(x='750',y='250')
        #==============================================================================================
        lname = ttk.Label(root,text = " Book Name")
        lname.place(x='350',y='350')
        lname.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
        ename = ttk.Entry(root,width=40)
        ename.place(x='550',y='350')

        laname = ttk.Label(root,text = " Author Name")
        laname.place(x='350',y='400')
        laname.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
        eaname = ttk.Entry(root,width=40)
        eaname.place(x='550',y='400')

        lid = ttk.Label(root,text = " No of Books")
        lid.place(x='350',y='450')
        lid.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
        eid = ttk.Entry(root,width=40)
        eid.place(x='550',y='450')

        lstr = ttk.Label(root,text = " Stream")
        lstr.place(x='350',y='500')
        lstr.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
        estr = ttk.Entry(root,width=40)
        estr.place(x='550',y='500')
        #==============================================================================================
        lsid = ttk.Label(root,text = " Search by Book Id")
        lsid.place(x='350',y='560')
        lsid.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
        esid = ttk.Entry(root,width=40)
        esid.place(x='550',y='560')
        #==============================================================================================
        submit = ttk.Button(root,text = 'Submit Details',width=20,command = lambda: database.book_ent(ename.get(),eaname.get(),int(eid.get()),estr.get()))
        submit.place(x='550',y='650')
        search = ttk.Button(root,text = 'Search Details',width=20,command = lambda: database.book_sea(esid.get()))
        search.place(x='400',y='650')

    book_ent()
#book_en()
