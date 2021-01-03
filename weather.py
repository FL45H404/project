import json
import requests
from win10toast import ToastNotifier

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
if __name__ == "__main__":
    weather1()