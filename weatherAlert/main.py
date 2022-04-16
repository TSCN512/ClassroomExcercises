OPENWEATHER_KEY = "getAKey"
account_sid = "youraccountidhere"
auth_token = "yourkeygoeshere"
import requests
import os
from twilio.rest import Client
print(os.environ.get("USERNAME")) #use api variable name as specified at footer, tester here
#weatherURL = "http://api.openweathermap.org/data/2.5/weather"
weatherURL = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat" : 40.712776,
    "lon" : -74.005974,
    #"q" : "New York City",
    "exclude" : "current,minutely,daily",
    "appid" : OPENWEATHER_KEY
}

response = requests.get(url=weatherURL, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_data = weather_data['hourly'][:12]
weather_condition = [item['weather'][0]['id'] for item in weather_data]

will_rain = False
for code in weather_condition:
    if int(code)<700: #we know codes in the 700 range and higher indicate no rain related reports
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Its gonna rain!",
            from_="yournumberhere",
            to="yourothernumberhere"
        )
    print(message.status)
#it was suggested to run this file as a scheduled task through pythonAnywhere

#security lesson here, using enviroment variables to separate critical data from possible exposed code
#checking the enviroment through a terminal/cmd prompt "env"
#defining a new enviroment variable "export var=mydata"
#use env to check successful export
#import the os module, use its function to get access to enviroment/its variables