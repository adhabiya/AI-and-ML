import cv2
cap= cv2.VideoCapture(1)
while True:
    key,img=cap.read()
    cv2.idmshow("test_video",img)
    cv2.waitKey(1)