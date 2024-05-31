import speech_recognition as aa
import pyttsx3
recognizer = aa.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    with aa.Microphone() as source:
        print("listening..")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            query = recognizer.recognize_google(audio)
            print("user said:",query)
            return query
        except aa.UnknownValueError:
            print("sorry, I didn't catch that.")
            return ""
        except aa.RequestError as e:
            print("could not request results; {0}".format(e))
            return ""
def handle_command(command):
    if "hello" in command:
        speak("Hello! how can I help you?")
    elif "what's the time" in command:
        speak("I'm sorry, I can't tell the time at the moment.")
    elif "goodbye" in command:
        speak("Sorry, I didn't understand that.")
        exit()
    else:
        speak("soory, I didn't understand that.")
if __name__ == "__main__":
    speak("Hello! I am your voice assistant.")
    while True:
        command = listen().lower()
        handle_command(command)