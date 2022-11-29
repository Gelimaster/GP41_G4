import pymysql



conn= pymysql.connect(
    user='root',
    password='root',
    host='127.0.0.1',
    port=4444, 
    database='gp41_db')

print(conn)
