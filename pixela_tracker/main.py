TOKEN = "tryYourToken"
USERNAME = "yourOwnUsername"
import requests
import datetime as dt

today = dt.datetime.now()
#today = str(today.date()).replace("-","") formatting into YYYYMMDD manually
today = today.strftime("%Y%m%d") #now using built in method
print(today)
pixela = "https://pixe.la/v1/users"
signup = {
    "token" : TOKEN, #password or API token, this will verify user
    "username" : USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor" : "yes"
}
#response = requests.post(url=pixela, json=signup)
#print(response.text)

graph_URL = f"{pixela}/{USERNAME}/graphs"
graph_id = "NameOfYourGraph"
graph_config = {
    "id" : graph_id, 
    "name" : "SomeTrackableExercise",
    "unit" : "attempts",
    "type" : "int",
    "color" : "ajisai"
}

header = {
    "X-USER-TOKEN" : TOKEN
}

#response = requests.post(url=graph_URL, json=graph_config, headers=header) #in lesson, headers was said to be in **kwargs, possibly previous
#print(response.text)

pixel_config = {
    "date" : today,
    "quantity" : "40"
}

#response = requests.post(url=f"{graph_URL}/{graph_id}", json=pixel_config, headers=header)
#print(response.text)

pixel_config = {
    "quantity" : "40"
}
print(f"{graph_URL}/{graph_id}/20220214") #put in the desired date, test or otherwise
#response = requests.put(url=f"{graph_URL}/{graph_id}/20220214", json=pixel_config, headers=header)
#response.raise_for_status()
#print(response.text)


response = requests.delete(url=f"{graph_URL}/{graph_id}/20220214", json=pixel_config, headers=header)
#just testing delete function here
print(response.text)