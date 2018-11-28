import pymysql
import pymysql.cursors
import pandas as pd


def dtb(df,table):
    conn = pymysql.connect(host = 'localhost',user = 'root')
    cur = conn.cursor()
    cur.execute('use books')
    cur.execute('create table if not exists '+table+'(Book_name char(60),Author_name char(60),no_of_books int,constraint primary key(Book_name,Author_name))')
    for i in range(len(df)):
        cur.execute("insert into "+table+" values('"+df['Book_name'][i]+"','"+df['Author_name'][i]+"',20)")
    conn.commit()
    conn.close()

def stu(df):
    conn = pymysql.connect(host = 'localhost',user = 'root')
    cur = conn.cursor()
    cur.execute('use books')
    cur.execute('create table if not exists students(Student_name char(40),Father_name char(40),roll int not null primary key,email char(40),Ph_no char(14),Address char(100),City char(40))')
    for i in range(len(df)):
        cur.execute("insert into students values('"+df['student_name'][i]+"','"+df['father_name'][i]+"',"+str(df['student_id'][i])+",'"+df['email'][i]+"','"+df['phone_no'][i]+"','"+df['address'][i]+"','"+df['city'][i]+"')")
    conn.commit()
    conn.close()


df = pd.read_csv('computer.csv')
df1 = pd.read_csv('civil.csv')
df2 = pd.read_csv('electrical.csv')
df3 = pd.read_csv('stu_data.csv')
#dtb(df,'comp')
#dtb(df1,'civ')
#dtb(df2,'elec')
#stu(df3)
