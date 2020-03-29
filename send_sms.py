from twilio.rest import Client
from credential import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

message = client.messages.create(to=my_cell, from_=my_twilio,
                             body='naru kal jete boleche')
#print response back from Twilio
