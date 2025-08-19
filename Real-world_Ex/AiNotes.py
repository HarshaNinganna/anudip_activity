import speech_recognition as sr
import pyttsx3
from transformers import pipeline

recognizer = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 160)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def speak(text):
    """Convert text to speech"""
    print(f"\n AI says: {text}\n")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture speech input"""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print(" Listening... Speak your meeting notes (say 'stop' to finish)...")
        audio = recognizer.listen(source, phrase_time_limit=30)
        try:
            query = recognizer.recognize_google(audio)
            print(f" You said: {query}")
            return query
        except Exception:
            print(" Couldn’t understand, please try again.")
            return ""

def summarize_text(text):
    """Summarize using Hugging Face model"""
    if len(text.split()) < 20: 
        return "Not enough content to summarize."
    summary = summarizer(text, max_length=60, min_length=25, do_sample=False)
    return summary[0]['summary_text']

def main():
    speak("Hello! I'm your AI Meeting Notes Assistant. Start speaking, and I’ll summarize.")
    all_text = ""

    while True:
        text = listen()
        if not text:
            continue
        if "stop" in text.lower():
            break
        all_text += " " + text

    if all_text.strip():
        print("\n Full Transcript:")
        print(all_text)

        summary = summarize_text(all_text)
        print("\n Summary:")
        print(summary)

        speak("Here’s a quick summary of your meeting:")
        speak(summary)
    else:
        speak("No notes captured. Try again!")

if __name__ == "__main__":
    main()
Ai
