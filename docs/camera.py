import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  

time.sleep(1)

if not cap.isOpened():
    print("❌ Cannot access camera. Try index 1 or 2, or check permissions.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
