APPID = "NiceID"
APPKEY = "AndANiceKey"
HEADERS = {
    "x-app-id" : APPID,
    "x-app-key" : APPKEY,
    "x-remote-user-id" : "0"
}
import datetime as dt
import requests

today = dt.datetime.now()
hour_min = today.strftime("%H:%M")
today = today.strftime("%d/%m/%Y")
input = input("Type in the exercise: ")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/GeneratedEndpoint/projectMyWorkouts/workouts"

sheety_header = {
    "Authorization" : "Bearer decentToken"
}
body = {
    "query" : input
}
response = requests.post(url=exercise_endpoint, json=body, headers=HEADERS) #remember that json= will be required for POST requests, not GET
#print(response.json()["exercises"][0])


for entry in response.json()["exercises"]:
    #print(f"Exercise: {entry['name']} \nDuration: {entry['duration_min']}\nEntry: {entry['nf_calories']}")

    body = {
        "workout" : {
            "date" : today,
            "time" : hour_min,
            "exercise" : entry['name'],
            "duration" : entry['duration_min'],
            "calories" : entry['nf_calories']
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=body, headers=sheety_header) #sheety dosen't need authentication through header, can be changed in sheety control panel
    print(sheety_response.text)