import smtplib
import datetime as dt
import random
import pandas

def send_email(quote):
    pass
    # my_email = "forstupid74@gmail.com"
    # password = "m8c8jxnWTFrkmEk"
    #
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=my_email, password=password,)
    #     connection.sendmail(
    #         from_addr=my_email,
    #         to_addrs="accounttest443@yahoo.com",
    #         msg=f"Subject:Hola\n\n
    #             {quote}"
    #     )

quotes = []

with open("quotes.txt", mode="r") as file:
    # Note to self List Comprehension, cause mi brain no remember anything
    quotes += [i for i in file.readlines()]
    # for i in file.readlines():
    #     quotes.append(i)

with open("birthdays.csv", mode="r") as file:
    pandas.read_csv(file)


now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()
date_of_birth = dt.datetime(year=1994, month=5, day=30, )


if date_of_birth.month == month and date_of_birth.weekday() == weekday:
    print("yey")
    # send_email(random.choice(quotes))



