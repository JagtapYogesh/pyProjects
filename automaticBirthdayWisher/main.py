import pandas
import smtplib
import random
import datetime as dt

MY_EMAIL = "<your_email>"
MY_PASSWORD = "<your_password>"

data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()

for index, row in data.iterrows():
    if now.month == row["month"] and now.day == row["day"]:
        letter_no = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_no}.txt", "r") as msg_file:
            msg_data = msg_file.read()
        msg_data = msg_data.replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=row["email"], msg=f"Subject:Happy Birthday!!!\n\n{msg_data}")