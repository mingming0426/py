import numpy as np
import cv2

# 实例化人脸分类器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#xml来源于资源文件。
# 读取测试图片
img = cv2.imread('faces.jpg',cv2.IMREAD_COLOR)
# 将原彩色图转换成灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 开始在灰度图上检测人脸，输出是人脸区域的外接矩形框
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=1)
# 遍历人脸检测结果
for (x,y,w,h) in faces:
    # 在原彩色图上画人脸矩形框
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
# 显示画好矩形框的图片
cv2.namedWindow('faces', cv2.WINDOW_AUTOSIZE)
cv2.imshow('faces',img)
# 等待退出键
cv2.waitKey(0)
# 销毁显示窗口
cv2.destroyAllWindows()
import cv2 as cv
import numpy as np
def face_detect_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = face_detector.detectMultiScale(gray, 1.2, 6)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv.imshow("result", image)

print("--------- Python OpenCV Tutorial ---------")

capture = cv.VideoCapture(0)
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
while(True):
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)#左右翻转
    face_detect_demo(frame)
    c = cv.waitKey(10)
    if c == 27: # ESC
        break
cv.waitKey(0)
cv.destroyAllWindows()