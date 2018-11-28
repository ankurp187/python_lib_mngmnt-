import pymysql
import pymysql.cursors
import pandas as pd

def book_rec(table):
    conn = pymysql.connect(host = 'localhost',user = 'root')
    cur = conn.cursor()
    cur.execute('use books')
    cur.execute('create table if not exists bkrecord(Book_code int not null auto_increment primary key,Book_name char(60),Author_name char(60),availability int,student_id char(16))')
    cur.execute('select * from '+table)
    det = cur.fetchall()
    #print(det)
    for i in range(len(det)):
        for j in range(20):
            cur.execute("insert into bkrecord(Book_name,Author_name,availability,student_id) values('"+det[i][0]+"','"+det[i][1]+"',1,'')")
    conn.commit()
    conn.close()

book_rec('comp')
book_rec('civ')
book_rec('elec')
