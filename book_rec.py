from tkinter import *
from tkinter import ttk
from tkinter import font
import pymysql
import pymysql.cursors


def bk_rkd():
    conn = pymysql.connect(host = 'localhost',user = 'root')
    cur = conn.cursor()
    cur.execute('use books')
    cur.execute('create table if not exists bkrecord(Book_code int not null auto_increment primary key,Book_name char(60),Author_name char(60),availability int,student_id char(16))')
    cur.execute('select * from bkrecord')
    det = cur.fetchall()
    cur.execute('desc bkrecord')
    data=cur.fetchall()
    deta=''
    for i in range(len(data)):
        deta=deta+'{'+data[i][0]+'}'
    root=Tk()
    root.geometry('1300x750+100+50')
    
    scrollbar=Scrollbar(root)
    scrollbar.pack(side=RIGHT,fill=Y)

    mylist = Listbox(root,yscrollcommand=scrollbar.set,font=('Helvetica',22,"bold"))
    mylist.insert(END,deta)
    
    mylist.config(width=1100)
    for i in range(len(det)):
        mylist.insert(END,det[i])
    mylist.pack(side=LEFT,fill=BOTH)
    scrollbar.config(command=mylist.yview)
