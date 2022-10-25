from flask import Flask, request ,render_template
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
    # textで指定されたパラメータをJsonに整形して返す
    #text = request.args.get('text', '')
    return render_template("index.html")

# 外部に公開できるようにポート開放
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
