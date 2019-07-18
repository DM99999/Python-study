import cv2
import matplotlib.pyplot as plt
from time import sleep

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
fig = plt.figure(figsize=(10, 6))
# 描画するデータ
x = []
y = []

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

def update(mean):
    """グラフを更新するための関数"""
    print(mean) #輝度の平均値を出力
    x.append(len(y))
    y.append(mean)
    # 折れ線グラフを描画する
    plt.ylim(0, 255)
    plt.plot(x, y)

while True:
    ret,frame = cap.read()
    cv2.imshow('Frame', frame)
    m = frame.mean() #輝度値の平均
    update(m)
    #ESCで終了
    k = cv2.waitKey(1)
    if k == 27:
        break
    sleep(1/fps) #毎フレームごとに計測
                   
cap.release()
cv2.destroyAllWindows()