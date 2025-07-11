import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "your_news_api_key_here"  # Replace with your actual News API key

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 
def aiprocess(c):
    client = OpenAI(
        api_key="your_api_key_here"  # Replace with your actual OpenAI API key
    )
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": c}
        ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    # Placeholder function body
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsdata.io/api/1/news?apikey={newsapi}&country=in&language=en")
        if r.status_code == 200:
                data = r.json()
                articles = data.get("results", [])
                if articles:
                    for article in articles[:5]:  # Read top 5 headlines
                        speak
                    (article.get("title", "No title found"))
                        
    else:
        output = aiprocess(c)
        speak(output)

if __name__ == "__main__":
    speak("initializing jarvis")
    # listen for the wake word "jarvis"
    while True:
        r = sr.Recognizer()
        
        print("Recognizing....")
        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=1)  # Helps with background noise
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                trigger = recognizer.recognize_google(audio).lower()
                if "jarvis" in trigger:
                    speak("Yes Prajyukta, how can I help you?")
            
                with sr.Microphone() as source:
                    print("Jarvis active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                
                processcommand(command)
                
        
        except Exception as e:
            print(" error; {0}".format(e))