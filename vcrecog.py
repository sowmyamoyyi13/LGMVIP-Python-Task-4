import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text to speech engine
engine = pyttsx3.init()

# Function to speak out the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's voice input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

# Function to perform actions based on user's commands
def assistant(query):
    if 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif 'search' in query:
        speak("What would you like me to search for?")
        search_query = listen()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
    elif 'stop' in query:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I didn't understand that command.")

# Main function to run the voice assistant
def main():
    speak("Hello! How can I assist you today?")
    while True:
        query = listen()
        if query:
            assistant(query)

if __name__ == "__main__":
    main()
