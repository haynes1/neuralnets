import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = os.environ['TWILIOACCOUNTSID']
auth_token = os.environ['TWILIOAUTHTOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="testing account",
                     from_=os.environ['TWILIOTESTNUMBER'],
                     to=os.environ['MYNUMBER']
                 )

print(message.sid)