import mysql.connector

cursor=""
conn=""
def register_user(username,mail,phone):
    #establishing the connection
    conn = mysql.connector.connect(
    user='root', password='password', host='127.0.0.1',port=4444, database='gp41_db')
    print("start connect")

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()  
    print("connection estabilished")

    
    # Preparing SQL query to INSERT a record into the database.
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


def register_yubi(result,username):
    #establishing the connection
    conn = mysql.connector.connect(
    user='root', password='password', host='localhost:4444', database='gp41_db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()  
    cursor2= conn.cursor()
    #ユーザのIDを取得
    sqlid="""SELECT"""+username +"""   FROM user_id("""


    # Preparing SQL query to INSERT a record into the database.
    sql = """INSERT INTO data_table(
    user_name,user_mailaddress,user_phone)
    VALUES ("""+username+""",example@gmail.com,080-XXXX-XXXX)"""

    try:
        # Executing the SQL command
        cursor.execute(sql)

        # Commit your changes in the database
        conn.commit()

        print("success")

    except:
        # Rolling back in case of error
        conn.rollback()

        # Closing the connection
        conn.close()

        print("error")

def register_kao(face,username):
    #establishing the connection
    conn = mysql.connector.connect(
    user='root', password='password', host='localhost:4444', database='gp41_db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()  

    # Preparing SQL query to INSERT a record into the database.
    sql = """INSERT INTO data_table(
    user_name,user_mailaddress,user_phone)
    VALUES ("""+username+""",example@gmail.com,080-XXXX-XXXX)"""

    try:
        # Executing the SQL command
        cursor.execute(sql)

        # Commit your changes in the database
        conn.commit()

        print("success")

    except:
        # Rolling back in case of error
        conn.rollback()

        # Closing the connection
        conn.close()

        print("error")


