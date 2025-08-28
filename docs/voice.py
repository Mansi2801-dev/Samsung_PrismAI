from gtts import gTTS
from googletrans import Translator
import os

gestures = ["Namaste", "Yes", "No", "come in"] 

translator = Translator()

output_folder = "tts_audio"
os.makedirs(output_folder, exist_ok=True)

for gesture in gestures:
    try:
        translated = translator.translate(gesture, dest="hi").text
        
        filename = os.path.join(output_folder, f"tts_{gesture}.mp3")
        tts = gTTS(text=translated, lang="hi")
        tts.save(filename)
        
        print(f"{gesture} -> {translated} | Saved: {filename}")
    except Exception as e:
        print(f"Error generating TTS for {gesture}: {e}")

print("✅ All Hindi gesture audio files pre-generated!")
