import cv2
import mediapipe as mp
import numpy as np
import joblib
import pygame
import os
import time

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

model = joblib.load("gesture_model(final).pkl")

pygame.mixer.init()

audio_folder = "tts_audio"

last_gesture = None
gesture_buffer = []
buffer_length = 5  
def speak_hindi(gesture):
    filename = os.path.join(audio_folder, f"tts_{gesture}.mp3")
    if os.path.exists(filename):
        try:
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Audio error for {gesture}: {e}")
    else:
        print(f"Audio file not found: {filename}")


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  

time.sleep(1)  

if not cap.isOpened():
    print("❌ Cannot access camera. Check permissions.")
    exit()

with mp_hands.Hands(min_detection_confidence=0.5,
                    min_tracking_confidence=0.5) as hands:

    while True:
        try:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                continue

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                coords = []
                for landmark in results.multi_hand_landmarks[0].landmark:
                    coords.append([landmark.x, landmark.y])

                coords = np.array(coords).flatten().reshape(1, -1)

                try:
                    gesture = model.predict(coords)[0]
                except Exception as e:
                    gesture = "(Prediction Error)"
                    print(f"Model error: {e}")

                gesture_buffer.append(gesture)
                if len(gesture_buffer) > buffer_length:
                    gesture_buffer.pop(0)

                if gesture_buffer.count(gesture) == buffer_length:
                    if gesture != last_gesture:
                        speak_hindi(gesture)
                        last_gesture = gesture

                cv2.putText(frame, f"{gesture}", (10, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("Sign to Voice", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        except Exception as e:
            print(f"Runtime error: {e}")
            time.sleep(0.1)

cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()


