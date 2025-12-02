import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='fbs'
)
# Create table
# sql='Create table emp(eid int primary key, ename varchar(30), dept varchar(30), salary int(10))'
# cursor=conn.cursor()
# cursor.execute(sql)


#INSERT TABLE
# sql="insert into emp(eid,ename,dept,salary) values(1,'John','IT',30000)"
# cursor=conn.cursor()
# cursor.execute(sql)
# conn.commit()

#SELECT FROM TABLE
sql='select * from emp'
cursor=conn.cursor()
cursor.execute(sql)
# print(cursor.fetchall())
# for row in cursor.fetchall():
    # print(row)
# print(cursor.fetchone())
