from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ea46e8597f3755b3ab123e5035cbaf34/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}
    # return all the data from the sheet.
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        print(data)
        self.destination_data = data["prices"]
        return self.destination_data
    # if the destination IATA code is empty. add one from flight search
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
