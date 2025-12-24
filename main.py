import os
os.system("cls")

# pip install opencv-python
import cv2

camera = cv2.VideoCapture(0)

while True:
    is_valid, image = camera.read()
    if is_valid:
        cv2.imshow("Ko'rsatish", image)
    
    if cv2.waitKey(1) & 0xfff == 32:
        break

cv2.destroyAllWindows()