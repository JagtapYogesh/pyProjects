import smtplib
SENDER_EMAIL_ADDR = "YOUR MAIL ID"
PASSWORD = "YOUR PASSWORD"

class NotificationManager:

    def __init__(self, user_data):
        self.user_details = user_data


    def send_notification(self, trip_data_details, city):
        msg_to_send = ""
        subject = f"Plan your next trip to {city}"
        for trip in trip_data_details:
            msg_to_send += f"Price: {trip['price']}\n"
            msg_to_send += f"Source City: {trip['cityFrom']}\n"
            msg_to_send += f"Source City Code: {trip['cityCodeFrom']}\n"
            msg_to_send += f"Destination City: {trip['cityTo']}\n"
            msg_to_send += f"Destination city Code: {trip['cityCodeTo']}\n"
            msg_to_send += f"Departure time in UTC: {trip['utc_departure']}\n"
            msg_to_send += f"Arrival time in UTC: {trip['utc_arrival']}\n"
            msg_to_send += f"********************************\n"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL_ADDR, password=PASSWORD)
            for user in self.user_details:
                connection.sendmail(from_addr=SENDER_EMAIL_ADDR, to_addrs=user["email"], msg=f"Subject:{subject}\n\nGreetings {user['firstName']},\n\nPlease look at the price drops of your desired destinations: \n{msg_to_send}\n\nThanks & Regards,\nFlight Deal Finder")
