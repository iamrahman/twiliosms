from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6cf0c7086c9b54da00a81bc501eb1d66"
# Your Auth Token from twilio.com/console
auth_token  = "4487617021039dbc0197afd2b5df6885"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917696342418", 
    from_="+13204336072",
    body="Hello, I am Rahman from Python Development!")

print(message.sid)
