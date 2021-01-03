import pyttsx3
import wikipedia
import datetime
import os
import webbrowser
import speech_recognition as sr
from tkinter import *
import subprocess  
import cv2
import weather as w
import xyz as msg
from PIL import ImageTk, Image
import requests
import json
from win10toast import ToastNotifier

print("INITIALIZING PROGRAM....")
path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
master = "RAGHAV"

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def Notification(result):
    noti=ToastNotifier()
    noti.show_toast("weather","Bengaluru-"+result,duration=10)
def weather1():
    apikey="76326b195dc753dc2a892a6fffc33369"
    city="Bengaluru"
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={apikey}"
    data=requests.get(url)
    result=data.json()
    result1=f"{result['main']['temp']}-C*, humidity-{result['main']['humidity']}\nwindspeed-{result['wind']['speed']}"
    # result2=result['main']['humidity']
    Notification(result1)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme(): 
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning" +master)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" +master)
    else:
        speak("Good Evening" +master)        

def takecommmand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio=r.listen(source)

    try:
        print("Recognizing......") 
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        speak("Say that again please")
        query= None
    return query.lower()
 


class Widget:
    def __init__(self):
       root = Tk()
       root.title('personal assistant(Mark-1)')
       root.config(background='Red')
       root.geometry('480x720')
       root.resizable(0, 0)
       self.compText = StringVar()
       self.userText = StringVar()
       self.userText.set('Click \'Run Assistant\' to Give commands')
       userFrame = LabelFrame(root, text="User", font=('Black ops one',10, 'bold'))
       userFrame.pack(fill="both", expand="yes")
       left2 = Message(userFrame, textvariable=self.userText, bg='#3B3B98', fg='white')
       left2.config(font=("Century Gothic", 24, 'bold'))
       left2.pack(fill='both', expand='yes')

       compFrame = LabelFrame(root, text="Jarvis", font=('Black ops one',10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg='#3B3B98',fg='white')
       left1.config(font=("Century Gothic", 24, 'bold'))
       left1.pack(fill='both', expand='yes')
       
       btn = Button(root, text='Run Jarvis', font=('Black ops one', 10, 'bold'), bg='#4b4b4b', fg='white',command=self.clicked).pack(fill='x', expand='no')
       btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='#4b4b4b', fg='white',command=root.destroy).pack(fill='x', expand='no')

       
       
       self.compText.set('Hello, I am Jarvis! What can i do for you Sir ??')

       root.bind("<Return>",self.clicked) # handle the enter key event of your keyboard
       root.mainloop()

    def clicked(self):
        i=0
        while i<1:
            print('Working')
            query = takecommmand()
            self.userText.set('Listening...')
            self.userText.set(query)
            query = query.lower()
            
            if 'wikipedia'in query:
                speak("Searching wikipedia......")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences =2)
                print(results)
                speak(results)

            elif "open youtube" in query:
                speak("opening youtube")
                webbrowser.get(path).open("youtube.com")

            elif 'open facebook' in query.lower():
                speak("opening facebook")  
                url = "facebook.com"
                webbrowser.get(path).open(url)  

            elif "open notepad" in query:
                speak("opening notepad")  
                os.system("start notepad")

            # elif "today weather" in query.lower():
            #     weather1()

            # elif 'open gmail' or 'gmail' in query.lower():
            #     speak("opening gmail") 
            #     webbrowser.get(path).open("gmail.com")

            elif 'open flipkart' in query.lower():
                speak("opening flipkart")  
                url = "flipkart.com"
                webbrowser.get(path).open(url)


            elif 'play music' or 'music' in query.lower():
                speak("Alright sir playing music")
                songs_dir="D:\\music\\songs" 
                songs=os.listdir(songs_dir)
                print(songs)
                os.startfile(os.path.join(songs_dir,songs[0]))

            elif "send mail" or "write a mail" in query.lower():
                msg.send()
            elif 'play videos' in query.lower():
                speak("Alright here's some entertainment for you sir")
                video_dir="E:\\video"
                videos=os.listdir(video_dir)
                os.startfile(os.path.join(video_dir,videos[0]))

            elif "log off" in query or "sign out" in query:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])
                
            elif "shut down" or "shutdown" in query:
                speak("Ok , your pc will shutdown in 10 sec make sure you exit from all applications")
                os.system("shutdown /s")

            elif "restart" or "re start" in query:
                speak("ok, restarting..")
                os.system("shutdown /r")
            i+=1
            # elif 'thank you' in query.lower():
            #     speak("Its my pleasure sir to always help you")


            # elif 'sorry' in query.lower():
            #     speak("well if you really are then say it to my master") 

        

            # elif 'ok google' in query.lower():
            #     speak("thats not me sir....i am jarvis")

            # elif 'hey siri' in query.lower():
            #     speak("i am jarvis sir,how can you forget something which is created by you sir")   

            # elif 'i want to be rich' in query.lower():
            #     speak("so do i") 

            # elif 'sing me a song' in query.lower():
            #     speak("Alright sir! i will try for you")
            #     songs_dir="D:\\music\\songs" 
                # songs=os.listdir(songs_dir)
            #     print(songs)
            #     os.startfile(os.path.join(songs_dir,songs[30]))  

            
    


if __name__ == '__main__':
    speak("INITIALIZING Project")
    wishme()
    widget = Widget()  

   