from twilio.rest import Client

TWILIO_SID = "ACb12e96b7fbe11188d85d102e056075c6"
TWILIO_AUTH_TOKEN = "4ad68919f053ff528a45f192ab4ca124"
TWILIO_VIRTUAL_NUMBER = "(575) 587-7547"
TWILIO_VERIFIED_NUMBER = "358451478838"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
