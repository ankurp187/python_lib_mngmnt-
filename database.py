import pymysql
import pymysql.cursors
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

def stud_ent(Student_name,Father_name,roll,email,Ph_no,Address,City):
    conn = pymysql.connect(host = 'localhost',user = 'root')
    a = conn.cursor()
    a.execute('create database if not exists books')
    a.execute('use books')
    a.execute('create table if not exists students(Student_name char(40),Father_name char(40),roll int not null primary key,email char(40),Ph_no char(14),Address char(100),City char(40))')
    try:
        a.execute("insert into students values('"+Student_name+"','"+Father_name+"',"+str(roll)+",'"+email+"','"+Ph_no+"','"+Address+"','"+City+"')")
        messagebox.showinfo("Welcome","information inserted for roll number "+str(roll))
    except(pymysql.err.IntegrityError):
        messagebox.showerror("Error","This roll number is alredy present")
    conn.commit()
    conn.close()


def stud_up(a,b,c):
    if(c=='S' and b!=""):
        conn = pymysql.connect(host = 'localhost',user = 'root')
        cur = conn.cursor()
        cur.execute('create database if not exists books')
        cur.execute('use books')
        cur.execute("update students set Student_name='"+b+"' where(roll="+str(a)+")")
        conn.commit()
        conn.close()
    if(c=='F' and b!=""):
        conn = pymysql.connect(host = 'localhost',user = 'root')
        cur = conn.cursor()
        cur.execute('create database if not exists books')
        cur.execute('use books')
        cur.execute("update students set Father_name='"+b+"' where(roll="+str(a)+")")
        conn.commit()
        conn.close()
    if(c=='E' and b!=""):
        conn = pymysql.connect(host = 'localhost',user = 'root')
        cur = conn.cursor()
        cur.execute('create database if not exists books')
        cur.execute('use books')
        cur.execute("update students set email='"+b+"' where(roll="+str(a)+")")
        conn.commit()
        conn.close()
    if(c=='P' and b!=""):
        conn = pymysql.connect(host = 'localhost',user = 'root')
        cur = conn.cursor()
        cur.execute('create database if not exists books')
        cur.execute('use books')
        cur.execute("update students set Ph_no='"+b+"' where(roll="+str(a)+")")
        conn.commit()
        conn.close()
    if(c=='A' and b!=""):
        conn = pymysql.connect(host = 'localhost',user = 'root')
        cur = conn.cursor()
        cur.execute('create database if not exists books')
        cur.execute('use books')
        cur.execute("update students set Address='"+b+"' where(roll="+str(a)+")")
        conn.commit()
        conn.close()
    if(c=='C' and b!=""):
        conn = pymysql.connect(host = 'localhost',user = 'root')
        cur = conn.cursor()
        cur.execute('create database if not exists books')
        cur.execute('use books')
        cur.execute("update students set City='"+b+"' where(roll="+str(a)+")")
        conn.commit()
        conn.close()
    

def admin_appl(user,pass_,eid):
    conn = pymysql.connect(host = 'localhost',user = 'root')
    p=-1
    a = conn.cursor()
    a.execute('create database if not exists books')
    a.execute('use books')
    a.execute('create table if not exists admins(User_name char(40),password char(40),user_id char(10) not null primary key)')
    a.execute('select * from adminappl')
    det = a.fetchall()
    for i in range(len(det)):
        if(det[i][1]==eid):
            p=i
    
    if(p != -1):
        try:
            a.execute("insert into admins values('"+user+"','"+pass_+"','"+det[p][1]+"')")
            messagebox.showinfo("Welcome","Welcome as admin,"+det[p][0])
        except(pymysql.err.IntegrityError):
            messagebox.showerror(title="Data Error",message="You are already an user")

    elif(p == -1):
        messagebox.showerror(title="Staff Error",message="You are not a library management staff")
    
    conn.commit()
    conn.close()


def book_ent(Book_name,Auth_name,num,stream):
    conn = pymysql.connect(host = 'localhost',user = 'root')
    a = conn.cursor()
    a.execute('create database if not exists books')
    a.execute('use books')
    a.execute('create table if not exists bkrecord(Book_code int not null auto_increment primary key,Book_name char(60),Author_name char(60),availability int,student_id char(16))')
    for i in range(num):
        a.execute("insert into bkrecord(Book_name,Author_name,availability,student_id) values('"+Book_name+"','"+Auth_name+"',1,'')")
    try:    
        a.execute("insert into "+stream+" values('"+Book_name+"','"+Auth_name+"',"+str(num)+")")
    except(pymysql.err.IntegrityError):
        a.execute("select no_of_books from "+stream+" where (Book_name='"+Book_name+"' and Author_name='"+Auth_name+"')")
        data = a.fetchone()
        num=data[0]+num
        a.execute("update "+stream+" set no_of_books="+str(num)+" where(Book_name='"+Book_name+"' and Author_name='"+Auth_name+"')")
    conn.commit()
    conn.close()


def book_sea(book_id):
    conn = pymysql.connect(host = 'localhost',user = 'root')
    a = conn.cursor()
    a.execute('use books')
    a.execute('select * from bkrecord where Book_code='+str(book_id))
    data = a.fetchone()

    root = Tk()
    root.geometry("500x500+100+100")
    root.title("Library Management System By Ankur Kumar Pandey")
    label = ttk.Label(root,text = str(data[0]))
    label.place(x='200',y='100')
    label.config(font=('Helvetica',22,"bold") ,background = 'violet',foreground = 'red')
    label = ttk.Label(root,text = "Book Name")
    label.place(x='100',y='200')
    label.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
    label = ttk.Label(root,text = str(data[1]))
    label.place(x='200',y='200')
    label.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'black')
    label = ttk.Label(root,text = "Author Name")
    label.place(x='100',y='250')    
    label.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
    label = ttk.Label(root,text = str(data[2]))
    label.place(x='200',y='250')
    label.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'black')
    label = ttk.Label(root,text = "Availability")
    label.place(x='100',y='300')    
    label.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
    label = ttk.Label(root,text = str(data[3]))
    label.place(x='200',y='300')
    label.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'black')
    label = ttk.Label(root,text = "Student Id")
    label.place(x='100',y='350')    
    label.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'red')
    label = ttk.Label(root,text = str(data[4]))
    label.place(x='200',y='350')
    label.config(font=('Helvetica',12,"bold") ,background = 'violet',foreground = 'black')
    conn.commit()
    conn.close()
