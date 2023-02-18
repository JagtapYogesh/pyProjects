from datetime import *

import requests

headers = {"apikey": "YOUR API KEY"}
KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
from_date = datetime.date(datetime.now()+timedelta(days=1)).strftime("%d/%m/%Y")
to_date = datetime.date(datetime.now()+timedelta(days=180)).strftime("%d/%m/%Y")
return_from = datetime.date(datetime.now()+timedelta(days=7)).strftime("%d/%m/%Y")
return_to = datetime.date(datetime.now()+timedelta(days=28)).strftime("%d/%m/%Y")


class FlightData:
    def __init__(self, to_location, max_price):
        self.to_location = to_location,
        self.max_price = max_price
        self.trips = []

    def search_for_trips(self, cityname):
        params = {
            "fly_from": "LON",
            "fly_to": self.to_location,
            "max_stopovers": 0,
            "date_from": from_date,
            "date_to": to_date,
            "return_from": return_from,
            "return_to": return_to,
            "curr": "GBP",
            "price_to": self.max_price
        }
        print(f"Finding your trips for {cityname}... Please wait")
        search_trip_response = requests.get(url=KIWI_ENDPOINT, params=params, headers=headers)
        for item in search_trip_response.json()["data"]:
            self.trips.append(item)

        if len(self.trips) > 0:
            return True
        else:
            return False
