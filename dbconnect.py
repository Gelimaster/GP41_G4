import mysql.connector

cursor=""
conn=""
def register_user(username,mail,phone):
    #establishing the connection
    conn = mysql.connector.connect(
    user='tsudura10th', password='U5RSSqJA', host='gp41db.mysql.database.azure.com',port=3306, database='gp41_db')
    print("start connect")

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()  
    print("connection estabilished")

    
    # Preparing SQL query to INSERT a record into the database.
    sql = """INSERT INTO user_table(
    user_name,user_mailaddress,user_phone)
    VALUES ('"""+username+"""','"""+mail+"""','"""+phone+"""')"""
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


def register_yubi(username,email,phone,fingerdata):
    #establishing the connection
    conn = mysql.connector.connect(
    user='tsudura10th', password='U5RSSqJA', host='gp41db.mysql.database.azure.com',port=3306, database='gb41_db')
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()  
    # Preparing SQL query to INSERT a record into the database.
    sql = """INSERT INTO user_table(
    user_name,user_mailaddress,user_phone)
    VALUES ('"""+username+"""','"""+email+"""','"""+phone+"""')"""
    print("executing query")
    print(sql)    
    try:
        # Executing the SQL command
        cursor.execute(sql)

        # Commit your changes in the database
        conn.commit()

        print("success")
        print("get success user id")
        sql="""SELECT @@IDENTITY"""
        print("executing query")
        print(sql) 
        try:
            cursor.execute(sql)
            id = cursor.fetchone()
            print(id[0])
            print("success")
            print("insert fingerdata")
            sql = """INSERT INTO user_table(user_id,data_finger)
            VALUES ('"""+id[0]+"""','"""+fingerdata+"""')"""
            print("executing query")
            print(sql) 
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

                print("error finger error")
                return False
        except:
            # Rolling back in case of error
            conn.rollback()

            # Closing the connection
            conn.close()

            print("error id fail")
            return False
    except:
        # Rolling back in case of error
        conn.rollback()

        # Closing the connection
        conn.close()

        print("user error")
        return False


def register_kao(face,username):
    #establishing the connection
    conn = mysql.connector.connect(
    user='tsudura10th', password='U5RSSqJA', host='gp41db.mysql.database.azure.com',port=3306, database='mysql')

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


