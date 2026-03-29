import speech_recognition as sr
import pyttsx3

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("\nJarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print("You:", query)
        return query.lower()
    except Exception as e:
        print("Sorry, could not understand.")
        return None