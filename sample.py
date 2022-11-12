import cv2
import base64
import numpy as np
import face_recognition
import io
from PIL import ImageFont, ImageDraw, Image
import glob
import mysql.connector

def main():
    connection = mysql.connector.connect(
        host='localhost', # 接続先
        port='3306',
        user='root', # mysqlのuser
        password='', # mysqlのpassword
        database='hoge', 
        use_pure=True,
    )

    # コネクションが切れたときに再接続してくれるように設定
    connection.ping(reconnect=True)
    
    # 接続できているかの確認
    print(connection.is_connected())


face_locations = []

#Base64でエンコードされたファイルのパス
target_file=r"sample.txt"
#デコードされた画像の保存先パス
image_file=r"decode.jpg"

with open(target_file, 'rb') as f:
    img_base64 = f.read()

#バイナリデータ <- base64でエンコードされたデータ  
img_binary = base64.b64decode(img_base64)
jpg=np.frombuffer(img_binary,dtype=np.uint8)

#raw image <- jpg
img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)
#画像を保存する場合
cv2.imwrite(image_file,img)

 # 画像を縦1/4 横1/4に圧縮
#small_frame = cv2.resize(image_file, (0,0), fx=0.25, fy=0.25)
# 顔の位置情報を検索
face_locations = face_recognition.face_locations(img)
if face_locations:
    print("画像に顔があります。")
else:
    print("画像に顔がありません。")

# 顔画像の符号化
#face_encodings = face_recognition.face_encodings(small_frame, face_locations)

#表示確認
# cv2.imshow('window title', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# for face_encoding in face_encodings:
#     # 顔画像が登録画像と一致しているか検証
#     matches = face_recognition.compare_faces(known_face_encodings, face_encoding, threshold)
#     name = "Unknown"

#     # 顔画像と最も近い登録画像を候補とする
#     face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#     best_match_index = np.argmin(face_distances)
#     if matches[best_match_index]:
#         name = known_face_names[best_match_index]

print("hello")