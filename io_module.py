import speech_recognition as sr
import pyttsx3



def listen_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return None


def listen_text():
    user_input = input("Please enter the task description: ")
    return user_input


def speak(text: str):
    if pyttsx3 is None:
        print(f"Gravies: {text}")
        return
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    print(f"Gravies: {text}")



