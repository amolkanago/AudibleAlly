import pyttsx3 # A text-to-speech library to convert text to speech
import speech_recognition as sr # A speech recognition library
import datetime # To work with date and time
import wikipedia # To access wikipedia data
import webbrowser # To access web browser
import os # To interact with operating system


# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Choose a voice that you prefer

# Customized assistant name
assistant_name = "AudibleAlly"

# Function to speak out audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Customized greetings based on the time of day
def custom_greetings():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak(f"Good morning, I am {assistant_name}!")
    elif 12 <= hour < 18:
        speak(f"Good afternoon, I am {assistant_name}!")
    else:
        speak(f"Good evening, I am {assistant_name}!")
    speak(f"How can I assist you today, sir?")

# Function to recognize and capture user's voice command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query



if __name__ == "__main__":
    custom_greetings()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'play music' in query:
            # Replace 'spotify:track:your_track_id' with the actual Spotify URI or URL of the song you want to play
            spotify_uri = 'https://open.spotify.com/track/73y649QhnXdcm6fRdvfraO?si=74f8d6faaba34adf'
            os.system(f'start spotify:{spotify_uri}')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\hp.DESKTOP-BM902D9\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'no thanks' in query:
            speak(f"Thank you for using {assistant_name}. Have a great day!")
            exit()