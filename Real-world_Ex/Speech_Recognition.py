import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

engine = pyttsx3.init()
engine.setProperty("rate", 160)  # speed
engine.setProperty("volume", 1)  # volume (0.0 to 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"️ You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        speak("Network error. Try again later.")
        return ""

def process_command(command):
    if "hello" in command:
        speak("Hello Harsha! How can I help you today?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "open youtube" in command:
        speak("Opening YouTube...")
        webbrowser.open("https://youtube.com")
    elif "open google" in command:
        speak("Opening Google...")
        webbrowser.open("https://google.com")
    elif "open github" in command:
        speak("Opening your GitHub profile...")
        webbrowser.open("https://github.com/HarshaNinganna")
    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I can't do that yet, but I'm learning every day.")

if __name__ == "__main__":
    speak("Hello, I am your Python voice assistant.")
    while True:
        command = listen()
        if command:
            process_command(command)
