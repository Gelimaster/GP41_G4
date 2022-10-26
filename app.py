from flask import Flask, request ,render_template
from scanfinger import *
app = Flask(__name__)

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
      myFP = FingerPrint()
    try:
        myFP.open()
        print("<p>Please touch the fingerprint sensor</p>")
        if myFP.identify():
            print("Hello! Master")
        else:
            print("Sorry! Man")
    finally:
        myFP.close()



    # textで指定されたパラメータをJsonに整形して返す
    #text = request.args.get('text', '')
    return render_template("index.html")

# 外部に公開できるようにポート開放
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
