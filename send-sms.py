from twilio.rest import Client

account_sid = "your_account_sid"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python!",
    from_="sender number",
    to="receiver number"
)

print("SMS Sent:", message.sid)
