API_KEY = "personalAPIkey"
endpoint = "http://tequila-api.kiwi.com/"
header = {
    "apikey" : API_KEY
}
import datetime as dt
import requests
tomorrow = dt.datetime.today() + dt.timedelta(days=1)
halfYear = tomorrow + dt.timedelta(days=180)
tomorrow = tomorrow.strftime("%d/%m/%Y")
halfYear = halfYear.strftime("%d/%m/%Y")

class FlightSearch:
    def searchForIATA(city):
        reply = requests.get(url=f"{endpoint}locations/query", params={"term" : city, "location_types" : "airport"}, headers=header)
        return reply.json()
    def searchTrips(fromID, toID, maxPrice):
        reply = requests.get(url=f"{endpoint}v2/search", params={"fly_from" : fromID, "fly_to" : toID, "price_to" : maxPrice, "date_from" : tomorrow, "date_to" : halfYear, "nights_in_dst_from" : 2, "flight_type" : "round", "max_stopovers":0}, headers=header)
        return reply.json()

