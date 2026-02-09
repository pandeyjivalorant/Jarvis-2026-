import speech_recognition as sr
import pyttsx3
import webbrowser

def speak(text):
    engine = pyttsx3.init()   # re-init every time (IMPORTANT)
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    print("Command:", c)
 
    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

if __name__ == "__main__":
    speak("Initializing Jarvis")

    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source)

            word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Ya")   

                with sr.Microphone() as source:
                    print("Listening command...")
                    audio = r.listen(source)

                command = r.recognize_google(audio)
                processcommand(command)

        except Exception as e:
            print("Error:", e)
