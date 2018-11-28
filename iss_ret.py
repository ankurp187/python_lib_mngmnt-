import pymysql
import pymysql.cursors
import pandas as pd

def issue(table,Book_name):
    status=0
    book_id=0
    conn = pymysql.connect(host = 'localhost',user = 'root')
    cur = conn.cursor()
    cur.execute('use books')
    cur.execute('select * from bkrecord')
    data = cur.fetchall()
    for i in range(len(data)):
        if(data[i][1]==Book_name and data[i][3]==1):
            status = 1
            book_id = data[i][0]
            break
    if(status==0):
        print('no book found')
    else:
        print(book_id)
        cur.execute('create table if not exists s'+table+'(Book_code int,Book_name char(60),Author_name char(60),constraint primary key(Book_name,Author_name))')
        cur.execute('select * from bkrecord where Book_code='+str(book_id))
        data = cur.fetchone()
        cur.execute("insert into s"+table+"(Book_code,Book_name,Author_name) values("+(str)(data[0])+",'"+data[1]+"','"+data[2]+"')")
        cur.execute('update bkrecord set availability=0,student_id='+table+' where(Book_code='+(str)(book_id)+')') 
    conn.commit()
    conn.close()

def retur(tab,bkid):
    conn = pymysql.connect(host = 'localhost',user = 'root')
    cur = conn.cursor()
    cur.execute('use books')
    cur.execute('update bkrecord set availability=1,student_id=NULL where(Book_code='+(str)(bkid)+')')
    cur.execute('delete from s'+tab+' where(Book_code='+(str)(bkid)+')')
    conn.commit()
    conn.close()
