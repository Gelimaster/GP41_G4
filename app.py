from flask import Flask, request ,render_template, redirect
from scanfinger import *
from opencmd import *
from dbconnect import *
import json
import hashlib
app = Flask(__name__)


#ハッシュ化式
#変数はstringじゃないといけないstr()
#変数名.sha256でハッシュ化する方法
#下の変数を利用(sha256)に.update(変数.encode("utf-8"))にデータを渡す
#sha256 = hashlib.sha256()
#そして使う時（print）はsha256.hexdigest()で返さないといけない
#※hexdigest()は変数に対してじゃなくて更新したsha256に対してする
#以下のリンクで詳細がわかる
# https://docs.python.org/ja/3/library/hashlib.html


@app.route('/')
def index():
    # textで指定されたパラメータをJsonに整形して返す
    #text = request.args.get('text', '')
   

    return render_template("index.html")
#登録
@app.route('/register',methods=["POST","GET"])
def register():
    if request.method == "POST":
        username= request.form["name"]       
        phone= request.form["mail"]
        email=request.form["phone"]
        if register_user(username,email,phone):
            return render_template("done.html")
        else:
            return render_template("index.html")    
            
@app.route('/test',methods=["POST","GET"])          
def test():
   return render_template("register.html")
    
# 顔認証のルート
@app.route('/kao')
def face_login():
    # textで指定されたパラメータをJsonに整形して返す
    #text = request.args.get('text', '')
    return render_template("index.html")

        

#指紋認証のルートログイン
@app.route('/yubi',methods=['POST','GET'])
def register_yubi():
    myFP = FingerPrint()
    try:
        myFP.open()
         #指情報
        fingerdata= myFP.identify()  
        #成功の場合
        if fingerdata :
            return render_template("Fingerlogin.html")
        #失敗の場合    
        else:
            return render_template("Failfinger.html")      
    finally:
        myFP.close()
    


#指紋認証のルート登録
@app.route('/registeryubi',methods=['POST','GET'])
#指コード利用する
def finger_login():
    myFP = FingerPrint()
    try:
        myFP.open()
         #指情報
        fingerdata= myFP.identify()        
    finally:
        myFP.close()




    # myFP = FingerPrint()
    # try:
    #     myFP.open()
    #     print("<p>Please touch the fingerprint sensor</p>")
    #     userfinger = myFP.identify()
    #     print("<p>processing</p>")
    #     return userfinger
    #     #check wich ID it is and log in
    # #     if userfing:
    # #     else:
    # finally:
    #     myFP.close()



    # textで指定されたパラメータをJsonに整形して返す
    #text = request.args.get('text', '')
    

# 外部に公開できるようにポート開放
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)