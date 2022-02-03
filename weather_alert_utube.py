import requests,time,threading
from win10toast import ToastNotifier
ipinfo=requests.get("https://ipapi.co/json").json()

coordinates={"lat": ipinfo["latitude"],"lon": ipinfo["longitude"]}

key="337e0427f1732f6e68bcb357ab57d189"

weatherAPI="https://api.openweathermap.org/data/2.5/weather"

def show_weather():
    weather=requests.get(weatherAPI,params={**coordinates,"appid":key}).json()
    condition=weather["weather"][0]["description"]
    temp1=weather["main"]["temp"]-273.15
    temp2=round(temp1,2)
    # print(weather)
    # print(condition)
    # print(temp2)
    print(f'Now its {condition}, currently {temp2}°C')
    notif=ToastNotifier()
    notif.show_toast("The current weather at Ghaziabad is",f'Now its {condition}, currently {temp2}°C')
    threading.Timer(10,show_weather).start()
    
show_weather()