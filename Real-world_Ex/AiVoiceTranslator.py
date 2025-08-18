import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Initialize recognizer, TTS engine, and translator
recognizer = sr.Recognizer()
engine = pyttsx3.init()
translator = Translator()

# Set voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # female voice if available
engine.setProperty("rate", 160)

def speak(text, lang="en"):
    """Speak the given text"""
    print(f"🔊 AI says: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen from mic"""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("🎤 Listening...")
        audio = recognizer.listen(source, phrase_time_limit=15)
        try:
            query = recognizer.recognize_google(audio)
            print(f"🗣 You said: {query}")
            return query
        except Exception:
            speak("Sorry, I didn’t catch that.")
            return ""

def main():
    speak("Hello! I'm your AI Translator. Speak in English, I will translate to Kannada.")
    
    while True:
        text = listen()
        if not text:
            continue
        
        if "exit" in text.lower():
            speak("Goodbye! Keep learning new languages.")
            break

        # Translate English → Kannada (you can change target language)
        translated = translator.translate(text, src="en", dest="kn")
        print(f"🌐 Translated: {translated.text}")
        speak(translated.text)

if __name__ == "__main__":
    main()
