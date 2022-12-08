from flask import Flask, request ,render_template, redirect
import base64
from scanfinger import *
from opencmd import *
from dbconnect import *
import subprocess as sp
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

#main page  DONE
@app.route('/')
def index():
   return render_template("index.html")

# decide if going to register finger or face　DONE
@app.route('/data',methods=["POST","GET"])
def aaa():
    if request.method == "POST":
        username= request.form["name"]       
        email= request.form["mail"]
        phone=request.form["phone"]
        data = {'username':username,'email':email,'phone':phone}
        return render_template("fingerface.html",data=data)

    # textで指定されたパラメータをJsonに整形して返す
    #text = request.args.get('text', '')

#登録 DONE
@app.route('/register',methods=["POST","GET"])
def register():
    if request.method == "POST":
        username= request.form["name"]       
        email= request.form["mail"]
        phone=request.form["phone"]
        result =register_user(username,email,phone)
        return result  
    
# 顔認証登録 inprogress....
@app.route('/face')
def face_login():
    # textで指定されたパラメータをJsonに整形して返す
    #text = request.args.get('text', '')
    return render_template("index.html")

        

#指紋認証登録 DONE
@app.route('/yubi',methods=['POST','GET'])
def yubi_register():
    if request.method == "POST":
        username= request.form["name"]       
        email= request.form["mail"]
        phone=request.form["phone"]
    myFP = FingerPrint()
    try:
        myFP.open()
         #指情報
        fingerdata= myFP.identify()  
        #成功の場合
        if fingerdata != False :
            finger=str(fingerdata)
            fingerdata= finger.encode('ascii')
            finger64=base64.b64encode(fingerdata)
            result=register_yubi(username,email,phone,finger64)
            return result
        #失敗の場合    
        else:
            return "指紋認証失敗"    
    finally:
        myFP.close()


# ログイン顔認証 inprogress....
@app.route('/loginface')
def login_face():
    return render_template("index.html")

#ログインページ done
@app.route('/login')
def login():
    return render_template("login.html")
    
# ログイン指紋認証 done
@app.route('/loginfinger',methods=['POST','GET'])
def login_finger():  
    myFP = FingerPrint()
    try:
        myFP.open()
        #指情報
        fingerdata= myFP.identify()  
        #成功の場合
        if fingerdata != False :
            finger=str(fingerdata)
            result=login_yubi(finger)
            return result
        #失敗の場合    
        else:
            return "指紋認証失敗"    
    finally:
        myFP.close()
    
        

# 外部に公開できるようにポート開放
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
