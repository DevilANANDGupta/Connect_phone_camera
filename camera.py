import cv2
import numpy as np
url = ('Ip url/video')
cap = cv2.VideoCapture(url)
while True:
    camera, frame = cap.read()
    if frame is not None:
        cv2.imshow("frame",frame)
    q=cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()
