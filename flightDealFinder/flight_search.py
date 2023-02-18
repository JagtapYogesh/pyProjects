import requests
headers = {"apikey": "YOUR API KEY"}
KIWI_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"


class FlightSearch:

    def __init__(self, iataCode):
        self.iataCode = iataCode

    def search_iata_code(self, city):
        data = {
            "term": city,
            "location_types": "city"
        }
        search_response = requests.get(url=KIWI_ENDPOINT, headers=headers, params=data)
        code = search_response.json()["locations"][0]["code"]
        return code
