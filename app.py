from flask import Flask, request ,render_template, redirect
from scanfinger import *
from opencmd import *
from dbconnect import *
import json
import hashlib
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
    # textで指定されたパラメータをJsonに整形して返す
    #text = request.args.get('text', '')
    # out = sp.run(["php", "templates/test.php"], stdout=sp.PIPE)
    # return out.stdout
   return render_template("index.html")

# decide if going to register finger or face
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
        if register_user(username,email,phone):
            return render_template("done.html")
        else:
            return render_template("index.html")    
            
@app.route('/test',methods=["POST","GET"])          
def test1():
   return  test()
    
# 顔認証登録
@app.route('/face')
def face_login():
    # textで指定されたパラメータをJsonに整形して返す
    #text = request.args.get('text', '')
    return render_template("index.html")

        

#指紋認証登録
@app.route('/yubi',methods=['POST','GET'])
def yubi_register():
    if request.method == "POST":
        username= request.form["name"]       
        email= request.form["mail"]
        phone=request.form["phone"]
    sha256 = hashlib.sha256()
    myFP = FingerPrint()
    try:
        myFP.open()
         #指情報
        fingerdata= myFP.identify()  
        #成功の場合
        if fingerdata != False :
            finger=str(fingerdata)
            sha256.update(finger.encode("utf-8"))
            fingerdata = sha256.hexdigest()
            if register_yubi(username,email,phone,fingerdata):
                return render_template("done.html")
            else:
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

# 外部に公開できるようにポート開放
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
