import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer=sr.Recognizer()
engine = pyttsx3.init()
newsAPI="87bcc1f7c19b423396930f8097689b9a"  

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open chat gpt" in c.lower():
        webbrowser.open("https://chatgpt.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        #Define the API URL with your API key
        #Send the GET request
        print("hi")
        response=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsAPI}")
        #Convert the response to JSON
        data=response.json()
        if data["status"] == "ok":
            articles = data["articles"]
            speak(" Top News Headlines:\n")
            for i, article in enumerate(articles[:10]):  # Speak top 10
                speak(f"{i+1}. {article['title']}")
        else:
            speak("Failed to fetch news. Please check your API key or request.")



if __name__=="__main__":
    speak("Initializing Jarvis...")
    while True:
    #Listen for the wake work "Jarvis"
    # obtain audio from the microphone
        r = sr.Recognizer()

        # recognize speech using Google Speech Recognition
        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)

            Initial_Command=r.recognize_google(audio)
            print("You said: "+ Initial_Command)
            if(Initial_Command.lower()=="jarvis"):   
                speak("Yes sir!")
                #Listening for Command
                with sr.Microphone() as source:
                    print("Jarvis activated!")
                    audio = r.listen(source,timeout=2,phrase_time_limit=2)

                command=r.recognize_google(audio)
                print("You said: "+ command)
                processCommand(command)





        except Exception as e:
            print("Error is coming; {0}".format(e))

     