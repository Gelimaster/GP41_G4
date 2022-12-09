# -*-coding : utf-8 -*-
import cv2
import base64
import numpy as np
import face_recognition
import io
from PIL import ImageFont, ImageDraw, Image
import glob
import mysql.connector
from mysql.connector import Error
import os

# connection = mysql.connector.connect(host='localhost',
#                                          database='face',
#                                          user='root',
#                                          password='root',
#                                          charset='utf8')


# with connection.cursor() as cursor:
#         # データ読み込み
#         sql = "SELECT data_face FROM data_table"
#         cursor.execute(sql)
#         result = cursor.fetchone()
#         print(result)
 
# # 終了処理
# cursor.close()

#     # コネクションが切れたときに再接続してくれるように設定
# connection.ping(reconnect=True)
    
#     # 接続できているかの確認
# if connection.is_connected() == True:
#     print("接続しました。")
# elif connection.is_connected() == False:
#     print("接続できませんでした。")

face_locations = []


# #追加箇所:カメラ起動し画像を保存
# #-------------------------------------------------------------------------------------------------------------------

# def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
#     cap = cv2.VideoCapture(device_num)

#     if not cap.isOpened():
#         return

#     os.makedirs(dir_path, exist_ok=True)
#     base_path = os.path.join(dir_path, basename)

#     while True:
#         ret, frame = cap.read()
#         cv2.imshow(window_name, frame)
#         key = cv2.waitKey(delay) & 0xFF
#         #cを押すと画像を保存
#         #
#         if key == ord('c'):
#             cv2.imwrite('{}.{}'.format(base_path, ext), frame)
#         elif key == ord('q'):
#             break

#     cv2.destroyWindow(window_name)


# # save_frame_camera_key(0, 'encode', 'encode')

# #Base64でエンコードする画像のパス
# target_file=r"encode/encode.jpg"
# #エンコードした画像の保存先パス
# encode_file=r"encode/encode.txt"

# with open(target_file, 'rb') as f:
#     data = f.read()
# #Base64で画像をエンコード
# encode=base64.b64encode(data)
# with open(encode_file,"wb") as f:
#     f.write(encode)

#     target_file=r"encode/encode.txt"

# #エンコードしたデータをtestにencode_txtとして格納
# encode_txt = [base64.b64encode(data)]

# connection.ping(reconnect=True)
#     # 接続できているかの確認
# if connection.is_connected() == True:
#     print("接続しました。")
# elif connection.is_connected() == False:
#     print("接続できませんでした。")

# with connection.cursor() as cursor:
# # データ読み込み
#         sql = ("UPDATE data_table SET data_face=%s WHERE data_id=1;")
#         param = (encode_txt)
#         cursor.execute(sql, param)
#         connection.commit()
#         result = cursor.fetchone()
#         print(result)

# # 終了処理
# cursor.close()
# f.close()

# #デコードされた画像の保存先パス
# image_file=r"decode.jpg"

# with open(target_file, 'rb') as f:
#     img_base64 = f.read()

# #バイナリデータ <- base64でエンコードされたデータ  
# img_binary = base64.b64decode(img_base64)
# jpg=np.frombuffer(img_binary,dtype=np.uint8)

# #raw image <- jpg
# img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)
# #画像を保存する場合
# cv2.imwrite(image_file,img)

# #表示確認
# cv2.imshow('window title', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #----------------------------------------------------------------------------------------------------------------


# #-------------------------------------------------------------------------------------------------------------------

# def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
#     cap = cv2.VideoCapture(device_num)

#     if not cap.isOpened():
#         return

#     os.makedirs(dir_path, exist_ok=True)
#     base_path = os.path.join(dir_path, basename)

#     while True:
#         ret, frame = cap.read()
#         cv2.imshow(window_name, frame)
#         key = cv2.waitKey(delay) & 0xFF
#         #cを押すと画像を保存
#         #
#         if key == ord('c'):
#             cv2.imwrite('{}.{}'.format(base_path, ext), frame)
#         elif key == ord('q'):
#             break

#     cv2.destroyWindow(window_name)


# # save_frame_camera_key(0, 'login_picture', 'login')

# #Base64でエンコードする画像のパス
# target_file=r"login_picture/login.jpg"
# #エンコードした画像の保存先パス
# encode_file=r"login_picture/login.txt"

# with open(target_file, 'rb') as f:
#     data = f.read()
# #Base64で画像をエンコード
# encode=base64.b64encode(data)
# with open(encode_file,"wb") as f:
#     f.write(encode)

#     target_file=r"login_picture/login.txt"


# with open(target_file, 'rb') as f:
#     img_base64 = f.read()
    
    


# #バイナリデータ <- base64でエンコードされたデータ  
# img_binary = base64.b64decode(img_base64)
# jpg=np.frombuffer(img_binary,dtype=np.uint8)

# #raw image <- jpg
# img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)
# #画像を保存する場合
# cv2.imwrite(image_file,img)

# # 画像を縦1/4 横1/4に圧縮
# #small_frame = cv2.resize(image_file, (0,0), fx=0.25, fy=0.25)
# # 顔の位置情報を検索
# face_locations = face_recognition.face_locations(img)
# if face_locations==False:
#     print("画像に顔がありません。")




# for fname in os.listdir(r"C:\Users\nhs90629\Documents\GitHub\GP41_G4\encode"):
#     face_locations = face_recognition.face_locations(img)
#     if face_locations ==False:
#         print("画像に顔がありません。")

# path = 'encode'
# images = []
# classNames = []
# myList = os.listdir(path)
# step1 画像読み込みとコンバート
# for cls in myList:
#     img_elon = face_recognition.load_image_file(f'{path}/{cls}')
#     img_elon = cv2.cvtColor(img_elon, cv2.COLOR_BGR2RGB)
#     img_test = face_recognition.load_image_file('login_picture/login.jpg')
#     img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)

#     # step2 顔認証
#     face_loc = face_recognition.face_locations(img_elon)[-1]

#     # 128次元の顔エンコーディングのリスト
#     encode_elon = face_recognition.face_encodings(img_elon)[0]
#     cv2.rectangle(img_elon, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)

#     face_loc_test = face_recognition.face_locations(img_test)[0]
#     encode_elon_test = face_recognition.face_encodings(img_test)[0]

#     # print(encode_elon_test)
#     cv2.rectangle(img_test, (face_loc_test[3], face_loc_test[0]), (face_loc_test[1], face_loc_test[2]), (255, 0, 255), 2)

#     # ２つの画像が同一人物かの判定
#     results = face_recognition.compare_faces([encode_elon], encode_elon_test)
#     # 値が小さい程マッチしている
#     face_dis = face_recognition.face_distance([encode_elon], encode_elon_test)

#     if results == [True]:
#         print(cls)
#         print("ログインしました。")
        
#         break
#     elif results == [False]:
#         print("ログインに失敗しました。")
            
def comparedata(database,faceid):
    # step1 画像読み込みとコンバート
        path='C:\Users\NHS90324\Downloads\\'+database

        img_elon = face_recognition.load_image_file('C:\Users\NHS90324\Downloads\\'+database)
        img_elon = cv2.cvtColor(img_elon, cv2.COLOR_BGR2RGB)
        
        img_test = face_recognition.load_image_file("C:\Users\NHS90324\Downloads\\"+faceid)
        img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)

        # step2 顔認証
        face_loc = face_recognition.face_locations(img_elon)[-1]

        # 128次元の顔エンコーディングのリスト
        encode_elon = face_recognition.face_encodings(img_elon)[0]
        cv2.rectangle(img_elon, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)

        face_loc_test = face_recognition.face_locations(img_test)[0]
        encode_elon_test = face_recognition.face_encodings(img_test)[0]

        # print(encode_elon_test)
        cv2.rectangle(img_test, (face_loc_test[3], face_loc_test[0]), (face_loc_test[1], face_loc_test[2]), (255, 0, 255), 2)

        # ２つの画像が同一人物かの判定
        results = face_recognition.compare_faces([encode_elon], encode_elon_test)
        # 値が小さい程マッチしている
        face_dis = face_recognition.face_distance([encode_elon], encode_elon_test)

        if results == [True]:
            print(cls)
            print("ログインしました。")
            return True

        elif results == [False]:
            print("ログインに失敗しました。")
            return False

# 8秒でwindowが閉じる設定
# cv2.startWindowThread()


# cv2.waitKey(8000)

# cv2.waitKey(1)
# cv2.destroyAllWindows()
# cv2.waitKey(1)


