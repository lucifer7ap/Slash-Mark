import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Set properties for the voice
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id)  # Change the index to select different voices
tts_engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None

def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        greet = "Good morning!"
    elif 12 <= hour < 18:
        greet = "Good afternoon!"
    else:
        greet = "Good evening!"
    speak(f"{greet} How can I assist you today?")

def open_website(url):
    webbrowser.open(url)

def perform_task(command):
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif 'open google' in command:
        speak("Opening Google")
        open_website("https://www.google.com")
    elif 'open youtube' in command:
        speak("Opening YouTube")
        open_website("https://www.youtube.com")
    elif 'open' in command:
        application = command.replace('open', '').strip()
        speak(f"Opening {application}")
        os.system(f"start {application}")
    elif 'shutdown' in command:
        speak("Shutting down the system")
        os.system("shutdown /s /t 1")
    else:
        speak("Sorry, I can’t perform that task yet.")

def main():
    greet_user()
    while True:
        command = listen()
        if command:
            if 'exit' in command or 'bye' in command:
                speak("Goodbye! Have a nice day.")
                break
            else:
                perform_task(command)

if __name__ == "__main__":
    main()
