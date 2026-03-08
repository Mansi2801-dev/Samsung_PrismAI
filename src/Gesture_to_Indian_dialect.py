import cv2
import mediapipe as mp
import numpy as np
import joblib
import pygame
import os
import time

# --- STEP 1: SMART PATHS ---
# Get the absolute path of the 'src' folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Get the Repo Root (one level up from 'src')
REPO_ROOT = os.path.dirname(BASE_DIR)

# Define paths to other folders
MODEL_PATH = os.path.join(REPO_ROOT, "docs", "gesture_model(final).pkl")
AUDIO_FOLDER = os.path.join(REPO_ROOT, "tts_audio")

# --- INITIALIZATION ---

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
try:
    model = joblib.load(MODEL_PATH)
    print(f"✅ Model loaded from: {MODEL_PATH}")
except Exception as e:
    print(f"❌ Could not find model at: {MODEL_PATH}")
    exit()



pygame.mixer.init()

# Use the smart path for audio
audio_folder = AUDIO_FOLDER

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
            start_bench = time.perf_counter()
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
                    end_bench = time.perf_counter()
                    latency_ms = (end_bench - start_bench) * 1000
                    print(f"Total Inference Latency: {latency_ms:.2f} ms")
                    cv2.putText(frame, f"Latency: {latency_ms:.1f}ms", (10, 80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
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


