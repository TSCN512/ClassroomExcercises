STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = "oneAPIKey"
NEWS_API_KEY = "anotherAPIKey"
account_sid = "youraccountidhere" #twilio
auth_token = "yourkeygoeshere" #twilio

#Using Tesla Stock as an example company to check
import datetime as dt
import requests
from twilio.rest import Client

def get_news(company):
    parameters = {
        "apiKey" : NEWS_API_KEY,
        "pageSize" : 3,
        "q" : company
    }
    response = requests.get(url="https://newsapi.org/v2/top-headlines", params=parameters)
    response.raise_for_status()
    news = ""
    for article in response.json()['articles']:
        news += "\nHeadline: "+article['title'] + "\nBrief: "+article['description']
    return news 

print(get_news(COMPANY_NAME.split()[0]))

def SMS_news(text):
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body=text,
            from_="yournumberhere",
            to="yourothernumberhere"
        )
    print(message.status)

parameters = {
    "function" : "TIME_SERIES_INTRADAY",
    "symbol" : STOCK,
    "interval" : "60min",
    "apikey" : ALPHA_API_KEY

}
current_day = dt.datetime.today()
yesterday = current_day.replace(day=current_day.day-1, hour=20, minute=0, second=0, microsecond=0)
two_days_ago = yesterday.replace(day=current_day.day-2) #datetime can get me properly formatted time keys from system clock

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
#print(response.json()['Time Series (60min)'][str(yesterday)]['4. close'])
yesterdays_close = float(response.json()['Time Series (60min)'][str(yesterday)]['4. close'])
day_before_yes_close = float(response.json()['Time Series (60min)'][str(two_days_ago)]['4. close'])

stock_change = yesterdays_close-day_before_yes_close
if abs(stock_change)>=yesterdays_close*.05:
    percent = round(stock_change/yesterdays_close *100) #saving percentage to use in f string
    if stock_change<0:
        percentage = f"🔻{percent}" #formatting here and below
    else:
        percentage = f"🔺{percent}%"
    header = STOCK + ": "+ percentage 
    sms_message = header + get_news(COMPANY_NAME)
    SMS_news(sms_message)
