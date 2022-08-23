##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
from pandas import DataFrame
import smtplib
import random

with open("birthdays.csv") as file:
    birthdays = pandas.read_csv(file)
    df = DataFrame.to_dict(birthdays)


now = dt.datetime.now()
month = now.month
weekday = now.weekday()
index = 0

for i in birthdays.index:
    birthday = dt.datetime(year=df["year"][i], month=df["month"][i], day=df["day"][i], hour=8)
    if birthday.month == month and birthday.weekday() == weekday:
        name = df["name"][i]
        index = i
        rand_letter = random.randint(1, 3)
        with open(f"letter_templates/letter_{rand_letter}.txt", mode="r") as file:
            txt = file.readline()
            letter = file.read()
            new_name = txt.replace("[NAME]", name)
            new_letter = new_name + letter


# Send the email
my_email = "forstupid74@gmail.com"
password = "m8c8jxnWTFrkmEk"
send_mail = df["email"][index]

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password,)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=send_mail,
        msg=f"Subject:{new_name}\n\n{new_letter}"
    )
