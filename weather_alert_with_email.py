import requests,time,threading,smtplib
from win10toast import ToastNotifier
ipinfo=requests.get("https://ipapi.co/json").json()

coordinates={"lat": ipinfo["latitude"],"lon": ipinfo["longitude"]}

key="337e0427f1732f6e68bcb357ab57d189"

weatherAPI="https://api.openweathermap.org/data/2.5/weather"
weather=requests.get(weatherAPI,params={**coordinates,"appid":key}).json()
condition=weather["weather"][0]["description"]
temp1=weather["main"]["temp"]-273.15
temp2=round(temp1,2)
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
    # threading.Timer(25,show_weather).start()
    
show_weather()

#------------------------------------------------------Email part---------------------------------------------------------------
from email.message import EmailMessage

EMAIL_ADDRESS = 'testingggg2002@gmail.com'
EMAIL_PASSWORD = 'testing2002'
msg = EmailMessage()
msg['Subject'] = 'Weather Alert!!!'
msg['From'] = EMAIL_ADDRESS 
msg['To'] = ['sk9910570374@gmail.com']
msg.set_content(f"The current weather at Ghaziabad is\n Now its {condition}, currently {temp2}°C")


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
    smtp.send_message(msg)