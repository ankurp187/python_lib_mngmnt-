from tkinter import *
from tkinter import ttk
from tkinter import font
import pymysql
import pymysql.cursors


def bk_detail():
    root=Tk()
    root.geometry('1300x750+100+50')
    conn = pymysql.connect(host = 'localhost',user = 'root')
    cur = conn.cursor()
    cur.execute('use books')
    cur.execute('select * from civ')
    det = cur.fetchall()
    cur.execute('desc civ')
    data=cur.fetchall()
    deta=''
    for i in range(len(data)):
        deta=deta+'{'+data[i][0]+'}'
    scrollbar=Scrollbar(root)
    scrollbar.pack(side=RIGHT,fill=Y)
    mylist = Listbox(root,yscrollcommand=scrollbar.set,font=('Helvetica',22,"bold"))
    for i in range(2):
        mylist.insert(END,'')
    mylist.insert(END,'CIVIL(civ)')
    mylist.insert(END,deta)
    for i in range(2):
        mylist.insert(END,'')
        
    mylist.config(width=1100)
    for i in range(len(det)):
        mylist.insert(END,det[i])
    mylist.pack(side=LEFT,fill=BOTH)
    scrollbar.config(command=mylist.yview)

    cur.execute('select * from comp')
    det = cur.fetchall()
    cur.execute('desc comp')
    data=cur.fetchall()
    deta=''
    for i in range(len(data)):
        deta=deta+'{'+data[i][0]+'}'
    for i in range(2):
        mylist.insert(END,'')
    mylist.insert(END,'COMPUTER SCIENCE(comp)')
    mylist.insert(END,deta)
    for i in range(2):
        mylist.insert(END,'')
        
    mylist.config(width=1100)
    for i in range(len(det)):
        mylist.insert(END,det[i])
    mylist.pack(side=LEFT,fill=BOTH)


    cur.execute('select * from elec')
    det = cur.fetchall()
    cur.execute('desc elec')
    data=cur.fetchall()
    deta=''
    for i in range(len(data)):
        deta=deta+'{'+data[i][0]+'}'
    for i in range(2):
        mylist.insert(END,'')
    mylist.insert(END,'ELECTRICAL(elec)')
    mylist.insert(END,deta)
    for i in range(2):
        mylist.insert(END,'')
        
    mylist.config(width=1100)
    for i in range(len(det)):
        mylist.insert(END,det[i])
    mylist.pack(side=LEFT,fill=BOTH)
