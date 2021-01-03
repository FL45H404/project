import smtplib
import pyautogui as p
# import sr1
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hunterzbca@gmail.com', 'Hunterz@123')
    server.sendmail('hunterzbca@gmail.com', to, content)
    server.close()

def send():
    # try:
    speak("enter recipient address")
    to=p.prompt(text='', title='To' , default='')
    speak("type your message.")
    content=p.prompt(text=' ',title="Compose email") 
    return sendEmail(to, content)
	# except Exception as e:
    #     print(e)
    #     sr1.speak("Sorry my friend harry bhai. I am not able to send this email")  