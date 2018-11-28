import pymysql
import pymysql.cursors


def save(table):
    conn = pymysql.connect(host = 'localhost',user = 'root')
    a = conn.cursor()
    a.execute('create database if not exists Books')
    a.execute('use Books')
    a.execute('create table if not exists '+table+'(book char(40),author char(40))')

def inserti(bookname,athname):
    conn = pymysql.connect(host = 'localhost',user = 'root')
    a = conn.cursor()
    a.execute('use books')
    a.execute("insert into tb1 values('"+bookname+"','"+athname+"')")
    conn.commit()
    conn.close()


#bn = input("Enter bookname")
#an = input("Enter author name")
#save('tb2')


