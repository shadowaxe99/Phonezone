import random
from pydub import AudioSegment
from pydub.playback import play
from twilio_setup import twilio_client
from eleven_labs_setup import eleven_labs_client

def simulate_background_noise(call_id):
    noise_level = random.randint(1, 3)
    noise = AudioSegment.from_file(f"noise_level_{noise_level}.mp3")
    twilio_client.calls(call_id).update(twiml=f'<Play>{noise}</Play>')

def simulate_voice_tone(call_id, user_id):
    user_data = eleven_labs_client.get_user_data(user_id)
    voice_tone = user_data['voice_tone']
    twilio_client.calls(call_id).update(twiml=f'<Say voice="{voice_tone}">Hello</Say>')

def mimic_real_call(call_id, user_id):
    simulate_background_noise(call_id)
    simulate_voice_tone(call_id, user_id)