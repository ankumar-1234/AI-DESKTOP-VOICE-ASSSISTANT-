import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import os
from requests import get, request
import wikipedia
import webbrowser
import sys
import time
import pyjokes 
import requests 



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
# print(voices[1].id)
engine.setProperty('voices', voices[len(voices) -1].id)


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("jarvis is listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        print("jarvis is Recognition...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please ....")
        return "none"
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak(f"good morning, its {tt}")
    elif hour>12 and hour<18:
        speak(f"good evening, its {tt}")

    else:
        speak(f"good evening sir , its {tt}")
    speak(" i am jarvis sir, your persnal artificial voice assistant plesae tell me how can i help you sir ")


# for news update
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=0382f12785fc4883ab77c2a8d6e37fea'

    main_page = requests.get(main_url).json()

    articles = main_page["articles"]

    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for an in articles:
        head.append(articles["title"])
    for i in range (len(day)):

        speak(f"today's {day[i]} news is: {head[i]}")


if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")
        
        elif "play music" in query:
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)                                             
            speak("according to wikipedia")                           
            speak(results)    
           
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open hackerrank" in query:
            webbrowser.open("www.hackerrank.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        
        elif "you can sleep" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

#to close any application           



        elif "closing notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("restart /s /t 5")
        
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()
        elif "hello jarvis" in query :
            speak("hello sir, i am good and how are you")
        
        elif "i am also good" in query:
            speak("hello sir please tell me how can i help you")

        elif "thank you jarvis" in query:
            speak("welcome sir")                                                                          