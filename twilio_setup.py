```python
from twilio.rest import Client

# Twilio API credentials
TWILIO_API_KEY = "your_twilio_api_key"
TWILIO_API_SECRET = "your_twilio_api_secret"

# Twilio client setup
client = Client(TWILIO_API_KEY, TWILIO_API_SECRET)

def initiate_call(user_phone_number, twilio_phone_number):
    call = client.calls.create(
        to=user_phone_number,
        from_=twilio_phone_number,
        url="http://demo.twilio.com/docs/voice.xml"
    )
    return call.sid

def end_call(call_sid):
    call = client.calls(call_sid).update(status='completed')
    return call.status

def fetch_call_details(call_sid):
    call = client.calls(call_sid).fetch()
    return call

def fetch_all_calls():
    calls = client.calls.list()
    return calls
```