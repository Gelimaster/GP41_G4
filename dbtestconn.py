import pymysql

# cursor=""
# conn=""
def register_user():
    print("start connection")
    # mydb = mysql.connector.connect(host='127.0.0.1',user='root',password='root',port=4444,database='gp41_db')
    # print(mydb)
    # #establishing the connection
    connection = pymysql.connect(host="localhost",database="gp41_db",port=4444,user="root",password="root",charset="utf8")
    # cursor = connection.cursor()
    # some other statements  with the help of cursor
    with connection.cursor() as cursor:
        sql="SELECT * FROM user_table "
        cursor.execute(sql)
        resul=cursor.fetchone()
        print(resul)
        return True
    if connection:
        print(connection)
        connection.close()
        return True
    else:
        connection.close()
        print("false")    
        return False 
    print("start connect")
    

    # #Creating a cursor object using the cursor() method
    cursor = conn.cursor()  
    print(conn)
    print("connection estabilished")

    # conn.close()
    # # Preparing SQL query to INSERT a record into the database.
    sql = """INSERT INTO user_table(
    user_name,user_mailaddress,user_phone)
    VALUES ("""+username+""","""+mail+""","""+phone+""")"""
    print("executing query")
    print(sql)
    try:
        # Executing the SQL command
        cursor.execute(sql)

        # Commit your changes in the database
        conn.commit()

        print("success")
        return True

    except:
        # Rolling back in case of error
        conn.rollback()

        # Closing the connection
        conn.close()

        print("error")
        return False

#"test","rafael@gmail.com","08036666666"

if __name__ == '__main__':
    print("start def")
    register_user()

    