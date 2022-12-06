## Bypusの使い方

# 準備

#### 1  プログラム
指紋認証と顔認証を取れるプログラム
(なければこのブランチのscanfinger.py(指紋認証プログラム)とXXXファイル（顔認証プログラム)を利用出来ます。

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
   phone_number* #電話番号
   fingerprint* #指紋認証
   faceid* #顔認証

#指紋認証登録
/registerfinger
   登録されてるユーザに指紋認証を登録

   送信必要パラメータ
   user_id #ユーザのID
   fingerprint #指紋認証

#顔認証登録
/registerface
   登録されているユーザに顔認証を登録
   
   送信必要パラメータ
   user_id #ユーザID
   faceid #顔認証

************ログイン************

#指紋認証でログイン
/loginfinger
   指紋認証でログイン

   送信必要パラメータ
   fingerprint #指紋認証

#顔認証でログイン
/loginface
   顔認証でログイン

   送信必要パラメータ
   faceid #顔認証 

************更新************

/updateuser
   ユーザの情報を変更したい場合

/updatefinger
   ユーザの指紋認証データの変更

/updateface
   ユーザの顔認証データを変更




************削除************
/deleteuser
   ユーザを削除する
/deletefinger
   ユーザの指紋認証データを削除

/deleteface
   ユーザの顔認証データを削除


*必須ではないパラメータ
```


## プロジェクトを自分のPCにダウンロードの仕方（クローンの仕方）

まずはVisual Studioのターミナルかコマンドプロンプトを開きクローンしたいフォルダまで移動します。

```bash
例：
PC/ユーザー/AndroidStudioProjects
cd C:\Users\NHS90324\AndroidStudioProjects
```

移動出来たら次のコマンドを実行する（githubをインストールしてないとできません）

```bash
 git clone https://github.com/tanakaho/IH4C_G3_android.git
```
これでインストールが開始されます。
インストール・更新はコマンドプロンプトかVSで行う必要があります（VSの場合は簡単にできます）







## GitHub 使い方

# GP41_G4

## プロジェクトを自分のPCにダウンロードの仕方（クローンの仕方）

まずはVisual Studioのターミナルかコマンドプロンプトを開きクローンしたいフォルダまで移動します。

```bash
例：
PC/ユーザー/AndroidStudioProjects
cd C:\Users\NHS90324\AndroidStudioProjects
```

移動出来たら次のコマンドを実行する（githubをインストールしてないとできません）

```bash
 git clone https://github.com/tanakaho/IH4C_G3_android.git
```
これでインストールが開始されます。
インストール・更新はコマンドプロンプトかVSで行う必要があります（VSの場合は簡単にできます）



#### 1  VSCodeのGithub Extensionをダウンロードしそこから作業する

#### 2  GitHub DesktopをインストールしそこからPull,pushのGitを操作する




### 1.1　Vscodeでやる人はここから

![img1](https://user-images.githubusercontent.com/50572505/119298062-38905a00-bc97-11eb-810a-87627aa79cf7.png)

 1ブランチの確認/変更
   
    左下の部分にブランチの確認と変更ができます


   ![img2](https://user-images.githubusercontent.com/50572505/119298469-10552b00-bc98-11eb-963c-dffc9fea2add.png)
   
    Create new branch...で新しいブランチを作成できます

 2 ChangeとStaged Change　
      
    ＋は変更や作ったものをStaged Changeにする（変更したものを確認したという意味）
    ↶は変更したものを前の状態に戻す（最後のコミット状態）

 3アイコン
      
    M は変更（既にある物を変更）
    A 新しく追加された（ファイル、写真が前のコミットに存在していない）


 4 コミットのコメントを入力する場所
    
    ・コミット名は　[]変更された部分の一言
    例　　　[Fix]ログインエラー   
           [Add]新規登録機能
    ルールではないが誰かが見ても理解できたらいい（各グループで話し合ってきめてもよし



  5 ✔をクリックするとStaged Changeされてる物をコミットする    

ここまでは***個人のPCです***GitHubにはまだアップロードしていません。

![スクリーンショット 2021-05-24 141003](https://user-images.githubusercontent.com/50572505/119299792-9d997f00-bc9a-11eb-9b84-29197b362321.png)

ここの🔄0↓1↑をクリックしない限りアップロードしませんのでご注文ください
    
    ↑　＝　アップロード
    ↓　＝　ダウンロード


これができたら完了です！


  


### 2.1　GitHub Desktopでやるかたこちら

### 1に戻る

