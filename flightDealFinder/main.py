from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data = DataManager()
while True:
    print("\n******Welcome to Flight Deal Finder******")
    print("Enter the value of firstname to NONE to exit")
    first_name = input("Enter your first name: ")
    if first_name.lower() == "none":
        break
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    re_email = input("Enter your email again: ")

    if email == re_email:
        status_code = data.insertuserinfo(first_name, last_name, email)
        if status_code == 200:
            print("Welcome to the club!!!!!")
        else:
            print("There was a problem. Please try again.")
    else:
        print("Email do not match")

users_data = data.getusersinfo()
notify_manager = NotificationManager(users_data)

for city in data.prices_response.json()["prices"]:
    if city["iataCode"] == "":
        print(city)
        trip = FlightSearch(city["iataCode"])
        code = trip.search_iata_code(city["city"])
        data.update_row(city["id"], code)

    else:
        check_availability = FlightData(city["iataCode"], city["lowestPrice"])
        status = check_availability.search_for_trips(city["city"])
        if status:
            trips_data = check_availability.trips
            notify_manager.send_notification(trips_data, city["city"])
        else:
            print(f"No available flights to {city['city']}")

