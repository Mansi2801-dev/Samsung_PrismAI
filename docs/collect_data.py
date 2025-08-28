import cv2
import mediapipe as mp
import csv
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

gesture_name = input("Enter gesture name (e.g., Namaste, come in, yes, no): ")

cap = cv2.VideoCapture(0)

f = open("gesture_dataset.csv", "a", newline="")
writer = csv.writer(f)

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.append(lm.x)
                    landmarks.append(lm.y)

                writer.writerow([gesture_name] + landmarks)

        cv2.imshow("Collecting Gesture Data", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
f.close()
cv2.destroyAllWindows()
