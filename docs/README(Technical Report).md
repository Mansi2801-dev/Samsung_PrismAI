# Gesture-to-Indian-Dialect

**Real-time hand gesture recognition with Hindi/Indian dialect voice output**

## Description
In this project, an experienced machine learning model is utilized to identify hand gestures through webcam.
and translate them live into Indian dialect.

## Modules Used

The libraries and modules listed below were used to realize **real-time gestures recognition** and **text-to-speech converting**. They collaborate to deal with **video capture**, **hand tracking**,**gesture prediction** and **audio playback**.

---

# Libraries and Modules Used

The following table summarizes the **libraries and modules** used in the project, their type, purpose, key functions, and role in the gesture-to-Indian-dialect system.
# Libraries and Modules Used

| **Library / Module** | **Type** | **Purpose** | **Key Functions** | **Role in Project** |
|---------------------|----------|------------|-----------------|-------------------|
| **OpenCV (cv2)** | External | Video capture & image processing | `VideoCapture()`, `cvtColor()`, `putText()`, `imshow()`, `destroyAllWindows()` | Captures webcam feed, converts frames to RGB, displays gesture labels, manages video windows |
| **MediaPipe (mp)** | External | Hand detection & tracking | `mp.solutions.hands`, `drawing_utils` | Detects 21 hand landmarks, draws landmarks, extracts coordinates for gesture prediction |
| **NumPy (np)** | External | Numerical computations & arrays | `array()`, `flatten()`, `reshape(1, -1)` | Converts hand landmarks into arrays, reshapes them for model input, ensures fast computation |
| **Joblib** | External | Model serialization | `load()` | Loads the trained gesture recognition model (`gesture_model(final).pkl`), predicts gestures in real-time |
| **Pygame** | External | Audio playback | `mixer.init()`, `mixer.music.load()`, `mixer.music.play()`, `mixer.quit()` | Plays pre-generated Hindi TTS audio files for recognized gestures |
| **OS** | Built-in | File & path handling | `path.join()`, `path.exists()` | Builds file paths, checks for audio file existence, prevents runtime errors |
| **Time** | Built-in | Timing & delays | `sleep()` | Adds short delays for camera stabilization and error handling, ensures smooth execution |

---

## Working of the code

### Current Implementation
The system demonstrates a complete **sign-to-speech pipeline**:

1. **Hand Detection:** Mediapipe identifies 21 hand landmarks (x, y coordinates).  
2. **Feature Vector:** Coordinates are flattened into a 42-dimensional vector.  
3. **Classification:** A K-Nearest Neighbors (KNN) classifier predicts gestures. Currently, it is trained on artificial data with labels like  “hello” and “thank you.”  
4. **Translation:** Predicted labels are translated into Hindi via Google Translate API.  
5. **Text-to-Speech:** The translation is spoken using pyttsx3.  
6. **Visualization:** Both English and Hindi labels are displayed on the video feed.

---

### Limitation
* Training data is synthetic (randomly generated), so predictions do not correspond to real gestures.  
* The classifier currently alternates between predefined labels without real-world meaning.

---

### Path to Real Gesture Recognition
1. **Data Collection:** Capture real hand landmark vectors for each gesture and save with labels in a dataset.  
2. **Model Training:** Train the classifier (KNN, SVM, Random Forest, or neural network) using multiple samples per gesture to capture variations.  
3. **Prediction & Deployment:** Load the trained model at runtime to classify, translate, and vocalize gestures accurately.

---

### Uniqueness and Gap

**Uniqueness:**  
This system integrates **real-time gesture recognition** with **Hindi speech synthesis**, going beyond simple hand tracking by combining machine learning classification with natural language voice output. It is specifically tailored for the **Indian context**, providing Hindi audio for gestures.

**Strengths:**  
- Balances **accuracy** (through gesture landmark buffering) and **usability** (real-time processing with audio feedback).  
- Provides a fully **end-to-end gesture-to-speech solution**.

**Potential Applications:**  
- Assisting **deaf-mute communication** (gesture → voice).  
- Gesture-controlled interfaces for **Indian users**.  
- **Cultural preservation**, e.g., recognizing mudras in Indian classical dance and explaining them.

---

### Future Scope

This gesture-to-Hindi-speech system offers significant potential for **inclusive technology** and can be extended across multiple domains:
- **Assistive Technology:** Supports deaf-mute users by converting hand gestures into Hindi (or other languages) speech.  
- **Cultural Preservation:** Digitizes and documents traditional gestures and mudras in Indian classical dance.  
- **Education & Learning:** Provides feedback in dance learning apps and physiotherapy exercises, aiding stroke or paralysis recovery.  
- **Multilingual Support:** Can be extended to English and regional Indian languages (Tamil, Bengali, Marathi, etc.).  
- **Smart Interfaces & Public Services:** Real-time gesture-to-speech translation in airports, banks, hospitals, and railway stations, enabling communication between differently-abled users and officials.  
- **Healthcare & Rehabilitation:** Gives real-time feedback and encouragement during physiotherapy or hand-movement exercises.

This system not only addresses accessibility challenges but also lays the foundation for **future AI-driven gesture-based interfaces** in education, healthcare, and cultural preservation.

---

### Summary

The code establishes a functional **end-to-end workflow**: hand detection → landmark extraction → classification → translation → speech output. With real gesture data, the system will provide accurate recognition and meaningful speech feedback.

