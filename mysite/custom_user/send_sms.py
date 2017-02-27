from twilio.rest import TwilioRestClient 

TWILIO_ACCOUNT_SID = 'AC4d7afd5857aa5b7a784611ebb7a6f5bb'
TWILIO_AUTH_TOKEN = 'dce0a9273bd34dd8d5016c601460841c'

client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) 

message = client.messages.create(
            to="+917845864524", 
            from_="2052363543", 
            body="Hello", 
            static_url='https://demo.twilio.com/owl.png', 