from flask import Flask, request ,render_template
from scanfinger import *
from opencmd import *
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


@app.route('/')
def index():
    # textで指定されたパラメータをJsonに整形して返す
    #text = request.args.get('text', '')
    out = sp.run(["php", "conn.php"], stdout=sp.PIPE)
    return out.stdout
   

    return render_template("index.html")

@app.route('/register',methods=["POST","GET"])
def register():
    name = request.args.get('message')
    return name
    if request.method == "POST":
        return render_template("index1.html")
    
# 顔認証のルート
@app.route('/kao')
def face_login():
    # textで指定されたパラメータをJsonに整形して返す
    #text = request.args.get('text', '')
    return render_template("index.html")

@app.route('/cmd')
def cmdopen():
   return test()
        



#指紋認証のルート
@app.route('/yubi',methods=['POST','GET'])
def finger_login():
    message = request.args.get('message')
    return message  



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
