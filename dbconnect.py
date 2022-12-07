import mysql.connector
cursor=""
conn=""
###########################################################################登録###########################################################################
#ユーザ登録
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
        result={'status':200,'username':username,'email':mail,'phone':phone}

        print("success")
        return result

    except:
        # Rolling back in case of error
        conn.rollback()

        # Closing the connection
        conn.close()

        print("error")
        result={'status':400,'errormessage':'入力エラー'}
        return result

#指紋認証登録
def register_yubi(username,email,phone,fingerdata):
    #データと接続
    conn = mysql.connector.connect(
    user='tsudura10th', password='U5RSSqJA', host='gp41db.mysql.database.azure.com',port=3306, database='gp41_db')
    
    #ポインター作成
    cursor = conn.cursor()  
    
    # SQL文 ユーザ登録
    sql = """INSERT INTO user_table(
    user_name,user_mailaddress,user_phone)
    VALUES ('"""+username+"""','"""+email+"""','"""+phone+"""')"""
    print("executing query")
    print(sql)    
    try:
        # SQL実行
        cursor.execute(sql)

        # SQLコミット
        conn.commit()
        print("commit success")
        print("get success user id")
        
        #SQL文　ユーザID取得
        sql="""SELECT @@IDENTITY"""
        print("executing query")
        print(sql) 
        try:
            #SQL実行
            cursor.execute(sql)

            #結果arrayからstringに変換
            result = cursor.fetchone()
            id=result[0]
            idint= str(id)
            print(idint)
            print("success id")
            print("insert fingerdata")
            
            #SQL文 指紋認証を登録
            sql = """INSERT INTO data_table(user_id,data_finger)VALUES("""+idint+""",'"""+fingerdata+"""')"""
            print("executing query")
            print(sql) 
            try:
                #SQL実行
                cursor.execute(sql)
                
                #SQLコミット
                conn.commit()
                print("success")

                #結果
                result={'status':200,'username':username,'email':email,'phone':phone}
                return result

            except:    
                 #エラーの場合ロールバック
                conn.rollback()

                #接続を着る
                conn.close()

                #結果
                print("error finger error")
                result={'status':400,'errormessage':'指紋データエラー'}
                return result
        except:
            # Rolling back in case of error
            conn.rollback()

            # Closing the connection
            conn.close()

            print("error id fail")
            result={'status':400,'errormessage':'通信エラー'}
            return result
    except:
        # Rolling back in case of error
        conn.rollback()

        # Closing the connection
        conn.close()

        print("user error")
        result={'status':400,'errormessage':'ユーザ情報エラー'}
        return result



#顔認証登録
def register_face(username,email,phone,facedata):
   #データと接続
    conn = mysql.connector.connect(
    user='tsudura10th', password='U5RSSqJA', host='gp41db.mysql.database.azure.com',port=3306, database='gp41_db')
    
    #ポインター作成
    cursor = conn.cursor()  
    
    # SQL文 ユーザ登録
    sql = """INSERT INTO user_table(
    user_name,user_mailaddress,user_phone)
    VALUES ('"""+username+"""','"""+email+"""','"""+phone+"""')"""
    print("executing query")
    print(sql)    
    try:
        # SQL実行
        cursor.execute(sql)

        # SQLコミット
        conn.commit()
        print("commit success")
        print("get success user id")
        
        #SQL文　ユーザID取得
        sql="""SELECT @@IDENTITY"""
        print("executing query")
        print(sql) 
        try:
            #SQL実行
            cursor.execute(sql)

            #結果arrayからstringに変換
            result = cursor.fetchone()
            id=result[0]
            idint= str(id)
            print(idint)
            print("success id")
            print("insert fingerdata")
            
            #SQL文 指紋認証を登録
            sql = """INSERT INTO data_table(user_id,data_face)VALUES("""+idint+""",'"""+facedata+"""')"""
            print("executing query")
            print(sql) 
            try:
                #SQL実行
                cursor.execute(sql)
                
                #SQLコミット
                conn.commit()
                print("success")

                #結果
                result={'status':200,'username':username,'email':email,'phone':phone}
                return result

            except:    
                 #エラーの場合ロールバック
                conn.rollback()

                #接続を着る
                conn.close()

                #結果
                print("error finger error")
                result={'status':400,'errormessage':'顔認証データエラー'}
                return result
        except:
            # Rolling back in case of error
            conn.rollback()

            # Closing the connection
            conn.close()

            print("error id fail")
            result={'status':400,'errormessage':'通信エラー'}
            return result
    except:
        # Rolling back in case of error
        conn.rollback()

        # Closing the connection
        conn.close()

        print("user error")
        result={'status':400,'errormessage':'ユーザ情報エラー'}
        return result

###########################################################################ログイン###########################################################################