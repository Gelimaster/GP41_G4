from flask import Flask, request ,render_template
from scanfinger import *
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
def hello_world():
    # textで指定されたパラメータをJsonに整形して返す
    #text = request.args.get('text', '')
    return render_template("index.html")

# 顔認証のルート
@app.route('/kao')
def face_login():
    # textで指定されたパラメータをJsonに整形して返す
    #text = request.args.get('text', '')
    return render_template("index.html")



#指紋認証のルート
@app.route('/yubi')
def finger_login():
    sha256 = hashlib.sha256()
    myFP = FingerPrint()
    try:
        myFP.open()
         #myFP.identify()
        fingerdata= myFP.identify()
        y=str(fingerdata)
        sha256.update(y.encode("utf-8"))
        data =[{'fingerprint':sha256.hexdigest()}]
        jsondata = json.dumps(data)
        return jsondata
        
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
    return render_template("index.html")

# 外部に公開できるようにポート開放
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
