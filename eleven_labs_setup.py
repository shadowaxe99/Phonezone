import requests
from call_handling import CallDataSchema, UserDataSchema

# Eleven Labs API credentials
ELEVEN_LABS_API_KEY = "your_api_key"
ELEVEN_LABS_API_SECRET = "your_api_secret"

# Base URL for Eleven Labs API
ELEVEN_LABS_BASE_URL = "https://api.elevenlabs.com"

# Function to authenticate with Eleven Labs API
def authenticate_with_eleven_labs():
    auth_data = {
        "apiKey": ELEVEN_LABS_API_KEY,
        "apiSecret": ELEVEN_LABS_API_SECRET
    }
    response = requests.post(f"{ELEVEN_LABS_BASE_URL}/auth", data=auth_data)
    response.raise_for_status()
    return response.json()["token"]

# Function to create a new call with Eleven Labs API
def create_call(user_data: UserDataSchema, call_data: CallDataSchema):
    token = authenticate_with_eleven_labs()
    headers = {"Authorization": f"Bearer {token}"}
    call_data = {
        "userId": user_data.user_id,
        "startTime": call_data.start_time,
        "endTime": call_data.end_time,
        "status": call_data.status
    }
    response = requests.post(f"{ELEVEN_LABS_BASE_URL}/calls", headers=headers, data=call_data)
    response.raise_for_status()
    return response.json()["callId"]

# Function to end a call with Eleven Labs API
def end_call(call_id):
    token = authenticate_with_eleven_labs()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.put(f"{ELEVEN_LABS_BASE_URL}/calls/{call_id}/end", headers=headers)
    response.raise_for_status()