import mysql.connector
import base64

#指紋認証ログイン
def get_face(facedata):
    #データと接続
    conn = mysql.connector.connect(
    user='tsudura10th', password='U5RSSqJA', host='gp41db.mysql.database.azure.com',port=3306, database='gp41_db')
    
    #ポインター作成
    cursor = conn.cursor()  
    
    # SQL文 指紋データ取得
    sql = """SELECT user_table.user_id,user_table.user_name,data_table.data_face FROM user_table,data_table"""
    print("executing query")
    print(sql)    
    try:
        # SQL実行
        cursor.execute(sql)
        
        #全ての結果を取得
        result = cursor.fetchall()
        print("total row number :",cursor.rowcount)
        
        #行の数を取得
        row =cursor.rowcount
        print(result)
        print("got face data")
        
        #指紋認証。。。。
        for x in range(row):
            #ここで画像がループしてるぜ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
            
            #復号化
            decoded= result[x][2].decode('ascii')
            
            #指紋比較
            if(decoded==facedata):
                #一致した場合
                login={'status':200, 'id' :result[x][0] ,'username':result[x][1]}  
        #結果           
        return login
    except:
        error={'status':200,'message':'指紋認証に失敗しました'}
        return error   
