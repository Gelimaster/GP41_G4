## Bypusの使い方

# 準備

#### 1  プログラム
指紋認証と顔認証を取れるプログラム
(なければこのブランチのscanfinger.py(指紋認証プログラム)とsample.py（顔認証プログラム)を利用出来ます。

#### 2  サーバ
これらのプログラムをサーバで実行できるようにしましょう


#### 3  ボタンのアイコン
ログインボタンのアイコンはiconf.jpgを利用してください。

#### 2  Bypus APIに接続方法
XXXXリンクにPostを送信することでAPIから返事が届きます。
APIエンドポイントは以下があります。

例) XXXXXX/registerに送信

```bash
************登録************

#ユーザ登録
/register
   ユーザを登録するポート
   
   送信必要パラメータ
   user_name #ユーザ名
   email #メールアドレス
   phone_number #電話番号

   APIからの返信
   json式 {
      status:200/400 #成功(200)か失敗(400)
      #成功した場合
      id:XX 
      username: XXXX #登録されたユーザ名
      email:XXX@mail.com　#登録されたユーザメールアドレス
      phone: 090XXXXXXXX　#登録されたユーザ番号
      #失敗の場合
      message: 入力エラー　#ユーザの入力ミス
   }

#指紋認証登録
/registerfinger
   登録されてるユーザに指紋認証を登録

   送信必要パラメータ
   user_name #ユーザ名
   email #メールアドレス
   phone_number #電話番号
   fingerprint #指紋認証

   APIからの返信
   json式 {
      status:200/400 #成功(200)か失敗(400)
      #成功した場合
      id:XX 
      username: XXXX #登録されたユーザ名
      email:XXX@mail.com　#登録されたユーザメールアドレス
      phone: 090XXXXXXXX　#登録されたユーザ番号
      #失敗の場合
      message: 入力エラー　#ユーザの入力ミス
   }

#顔認証登録
/registerface
   登録されてるユーザに指紋認証を登録

   送信必要パラメータ
   user_name #ユーザ名
   email #メールアドレス
   phone_number #電話番号
   faceid #指紋認証

   APIからの返信
   json式 {
      status:200/400 #成功(200)か失敗(400)
      #成功した場合
      id:XX 
      username: XXXX #登録されたユーザ名
      email:XXX@mail.com　#登録されたユーザメールアドレス
      phone: 090XXXXXXXX　#登録されたユーザ番号
      #失敗の場合
      message: 入力エラー　#ユーザの入力ミス
   }

************ログイン************

#指紋認証でログイン
/loginfinger
   指紋認証でログイン

   送信必要パラメータ
   fingerprint #指紋認証
      登録されてるユーザに指紋認証を登録
   APIからの返信
   json式 {
      status:200/400 #成功(200)か失敗(400)
      #成功した場合
      id:XX 
      username: XXXX #登録されたユーザ名
      email:XXX@mail.com　#登録されたユーザメールアドレス
      phone: 090XXXXXXXX　#登録されたユーザ番号
      #失敗の場合
      message: 入力エラー　#指紋認証に失敗
   }

#顔認証でログイン
/loginface
   顔認証でログイン

   送信必要パラメータ
   faceid #顔認証 
   登録されてるユーザに指紋認証を登録

   APIからの返信
   json式 {
      status:200/400 #成功(200)か失敗(400)
      #成功した場合
      id:XX 
      username: XXXX #登録されたユーザ名
      email:XXX@mail.com　#登録されたユーザメールアドレス
      phone: 090XXXXXXXX　#登録されたユーザ番号
      #失敗の場合
      message: 入力エラー　#顔認証失敗
   }
```



## プロジェクトを自分のPCにダウンロードの仕方（クローンの仕方）

まずはVisual Studioのターミナルかコマンドプロンプトを開きクローンしたいフォルダまで移動します。

```bash
例：
PC/ユーザー/ダウンロード先ファイル
cd C:\Users\ダウンロード先ファイル
```

移動出来たら次のコマンドを実行する（githubをインストールしてないとできません）

```bash
 git clone https://github.com/Gelimaster/GP41_G4.git
```
これでインストールができます。


