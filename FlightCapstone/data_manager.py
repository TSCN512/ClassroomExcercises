endpoint = "https://api.sheety.co/generatedDirectory/flightDealsProject/prices/" #add row to endpoint to access it
API_TOKEN = "Bearer personalAPItoken" #follows token format
header = {
    "Authorization" : API_TOKEN
}
import requests
class DataManager:
    def column_fill(column_list):
        for entry in range(0,len(column_list)):
            response = requests.put(url=f"{endpoint}{entry+2}", json={"price" : {"iataCode" : column_list[entry]}}, headers=header)
            print(response.text)    
        return "Complete"
    def get_cityList():
        response = requests.get(url=f"{endpoint}", headers=header)
        return response.json()

#response = requests.put(url=f"{endpoint}2", json={"price" : {"iataCode" : "PAR"}}, headers=header)
#print(response.json())