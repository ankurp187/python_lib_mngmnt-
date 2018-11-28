from tkinter import *
from tkinter import ttk
from tkinter import font
import pymysql
import pymysql.cursors
from tkinter import messagebox
import database
import iss_ret


c=0

def iss():
    global c
    root2=Tk()
    root2.geometry("400x250+600+300")
    label = ttk.Label(root2,text = "Enter book name")
    label.place(x='10',y='80')
    label.config(font=('Helvetica',14,"bold") ,background = 'cyan',foreground = 'black')
    change = ttk.Entry(root2,width=20)
    change.place(x='50',y='170')
    submit = ttk.Button(root2,text="Issue",command=lambda:[iss_ret.issue(str(c),change.get()),root2.destroy()])
    submit.place(x='250',y='170')

def ret():
    global c
    root2=Tk()
    root2.geometry("400x250+600+300")
    label = ttk.Label(root2,text = "Enter book no.")
    label.place(x='10',y='80')
    label.config(font=('Helvetica',14,"bold") ,background = 'cyan',foreground = 'black')
    change = ttk.Entry(root2,width=20)
    change.place(x='50',y='170')
    submit = ttk.Button(root2,text="Submit",command=lambda:[iss_ret.retur(str(c),int(change.get())),root2.destroy()])
    submit.place(x='250',y='170')


def f1(event):
    global c
    up_field=event.widget.cget("text")
    root1=Tk()
    root1.geometry("400x250+600+300")
    label = ttk.Label(root1,text = "Enter"+up_field)
    label.place(x='10',y='80')
    label.config(font=('Helvetica',14,"bold") ,background = 'cyan',foreground = 'black')
    change = ttk.Entry(root1,width=20)
    change.place(x='50',y='170')
    submit = ttk.Button(root1,text="Submit",command=lambda:[database.stud_up(int(c),change.get(),up_field[1]),root1.destroy()])
    submit.place(x='250',y='170')

def Hinfo():
    messagebox.showinfo("INFORMATION","Double Click The Raised Labels To Update Values")

def stud_ui(a,b,c,d,e,f,g):
    root = Tk()
    root.geometry("1100x750+75+50")
    root.config(background = 'cyan')
    root.title("Library Management System By Ankur Kumar Pandey")

    label = ttk.Label(root,text = "Student Details")
    label.place(x='450',y='100')
    label.config(font=('Helvetica',27,"bold") ,background = 'violet',foreground = 'red')

    menubar = Menu(root)
    filemenu = Menu(menubar,tearoff=0)
    filemenu.add_command(label="Info",command=Hinfo)
    menubar.add_cascade(label="HELP",menu=filemenu)
    root.config(menu=menubar)
    #==============================================================================================
    lname = ttk.Label(root,text = " Student Name",relief=RAISED)
    lname.place(x='350',y='250')
    lname.config(font=('Helvetica',15,"bold") ,background = 'violet',foreground = 'red')
    lname.bind('<Double-Button-1>',f1)
    ename = ttk.Label(root,text = a)
    ename.place(x='550',y='250')
    ename.config(font=('Helvetica',12,"bold"))

    lfname = ttk.Label(root,text = " Father's Name",relief=RAISED)
    lfname.place(x='350',y='300')
    lfname.config(font=('Helvetica',15,"bold") ,background = 'violet',foreground = 'red')
    lfname.bind('<Double-Button-1>',f1)
    efname = ttk.Label(root,text = b)
    efname.place(x='550',y='300')
    efname.config(font=('Helvetica',12,"bold"))

    lroll = ttk.Label(root,text = " Student Roll No")
    lroll.place(x='350',y='350')
    lroll.config(font=('Helvetica',15,"bold") ,background = 'violet',foreground = 'red')
    eroll = ttk.Label(root,text = int(c))
    eroll.place(x='550',y='350')
    eroll.config(font=('Helvetica',12,"bold"))

    lemail = ttk.Label(root,text = " Email",relief=RAISED)
    lemail.place(x='350',y='400')
    lemail.config(font=('Helvetica',15,"bold") ,background = 'violet',foreground = 'red')
    lemail.bind('<Double-Button-1>',f1)
    eemail = ttk.Label(root,text=d)
    eemail.place(x='550',y='400')
    eemail.config(font=('Helvetica',12,"bold"))

    lphn = ttk.Label(root,text = " Phone Number",relief=RAISED)
    lphn.place(x='350',y='450')
    lphn.config(font=('Helvetica',15,"bold") ,background = 'violet',foreground = 'red')
    lphn.bind('<Double-Button-1>',f1)
    ephn = ttk.Label(root,text=e)
    ephn.place(x='550',y='450')
    ephn.config(font=('Helvetica',12,"bold"))
    #==============================================================================================
    ladd = ttk.Label(root,text = " Address",relief=RAISED)
    ladd.place(x='350',y='500')
    ladd.config(font=('Helvetica',15,"bold") ,background = 'violet',foreground = 'red')
    ladd.bind('<Double-Button-1>',f1)
    eadd = ttk.Label(root,text=f)
    eadd.place(x='550',y='500')
    eadd.config(font=('Helvetica',12,"bold"))

    lcity = ttk.Label(root,text = " City",relief=RAISED)
    lcity.place(x='350',y='550')
    lcity.config(font=('Helvetica',15,"bold") ,background = 'violet',foreground = 'red')
    lcity.bind('<Double-Button-1>',f1)
    ecity = ttk.Label(root,text=g)
    ecity.place(x='550',y='550')
    ecity.config(font=('Helvetica',12,"bold"))

    issue = ttk.Button(root,text="Issue book",command=iss)
    issue.place(x='900',y='100')

    retur = ttk.Button(root,text="Return book",command=ret)
    retur.place(x='900',y='150')



def sear_stud(sid):
    global c
    conn = pymysql.connect(host = 'localhost',user = 'root')
    a = conn.cursor()
    a.execute('create database if not exists books')
    a.execute('use books')
    a.execute('select * from students where(roll='+str(sid)+')')
    data = a.fetchone()
    c=data[2]
    stud_ui(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
    #print(data)
    conn.commit()
    conn.close()

def base():
    root = Tk()
    root.geometry("400x250+600+300")
    root.config(background = 'cyan')
    root.title("Library Management System By Ankur Kumar Pandey")
    label = ttk.Label(root,text = "Enter Student Id To Get The Information")
    label.place(x='10',y='80')
    label.config(font=('Helvetica',14,"bold") ,background = 'cyan',foreground = 'black')
    s_id = ttk.Entry(root,width=20)
    s_id.place(x='50',y='170')
    submit = ttk.Button(root,text="Search",command=lambda:[sear_stud(int(s_id.get())),root.destroy()])
    submit.place(x='250',y='170')
