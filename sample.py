import cv2
import base64
import numpy as np
import io

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

#表示確認
# cv2.imshow('window title', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print("hello")