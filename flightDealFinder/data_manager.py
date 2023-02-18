import requests
SHETTY_PRICES_ENDPOINT = "<prices_endpoint>"
SHEETY_USERS_ENDPOINT = "<user_endpoint>"

class DataManager:
    def __init__(self):
        self.prices_response = requests.get(url=SHETTY_PRICES_ENDPOINT)


    def update_row(self, id, code):
        data = {
            "price": {
                "iataCode": code
            }
        }
        update_response = requests.put(url=f"{SHETTY_PRICES_ENDPOINT}/{id}", json=data)

    def insertuserinfo(self, firstname, lastname, email):
        data = {
            "user": {
                "firstName": firstname,
                "lastName": lastname,
                "email": email
            }
        }
        insert_user_response = requests.post(url=SHEETY_USERS_ENDPOINT, json=data)
        return insert_user_response.status_code

    def getusersinfo(self):
        get_user_response = requests.get(url=SHEETY_USERS_ENDPOINT)
        return get_user_response.json()["users"]
