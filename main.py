from tkinter import *
from tkinter import ttk
from tkinter import font
import database
import book_rec
import book_details
import stu_rec
import book_det
import stu_det
import stu_lib


def sign_up():
    def sub(event):
        pas.config(show='*')

    def sub1(event):
        pas.config(show="")
    
    root1=Tk()
    root1.geometry("700x450+75+50")
    label1 = Label(root1,text="username",width=40,font=("bold",10))
    label1.place(x=0,y=100)
    user = Entry(root1,width=40)
    user.place(x=200,y=100)

    label2 = Label(root1,text="password",width=40,font=("bold",10))
    label2.place(x=0,y=150)
    pas = Entry(root1,width=40)
    pas.place(x=200,y=150)
    pas.config(show='*')

    label3 = Label(root1,text="enroll_id",width=40,font=("bold",10))
    label3.place(x=0,y=200)
    eid = Entry(root1,width=40)
    eid.place(x=200,y=200)

    sho = Button(root1,text="SHOW")
    sho.place(x=550,y=150)
    sho.bind('<ButtonPress-1>',sub1)
    sho.bind('<ButtonRelease-1>',sub)

    ad = ttk.Button(root1,text="Submit Details",command=lambda:[database.admin_appl(user.get(),pas.get(),eid.get()),root1.destroy()])
    ad.place(x=150,y=300)


root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="close")
menubar.add_cascade(label="file",menu=filemenu)
root.config(menu=menubar)

root.geometry("1150x750+75+50")
root.config(background = 'cyan')
root.title("Library Management System By Ankur Kumar Pandey")

label = ttk.Label(root,text = "Library Management System",relief=RAISED)
label.place(x='200',y='100')
label.config(font=('Helvetica',36,"bold") ,background = 'violet',foreground = 'red')
#==============================================================================================
signup = Button(root,text = 'Admin Sign Up',width=20,relief=RAISED,command=sign_up)
signup.place(x='950',y='120')

studet = ttk.Button(root,text = 'Enter Student Details',width=50,command=stu_det.stud_fill)
studet.place(x='150',y='250')

stulib = ttk.Button(root,text = 'Student Library Detail',width=50,command=stu_lib.base_lib)
stulib.place(x='600',y='250')

sturec = ttk.Button(root,text = 'Student Record',width=50,command=stu_rec.base)
sturec.place(x='150',y='400')

bookrec = ttk.Button(root,text = 'Book Record',width=50,command=book_rec.bk_rkd)
bookrec.place(x='600',y='400')

bookdet = ttk.Button(root,text = 'Book Details',width=50,command=book_details.bk_detail)
bookdet.place(x='150',y='550')

bookentry = ttk.Button(root,text = 'Book Entry',width=50,command=book_det.book_en)
bookentry.place(x='600',y='550')
