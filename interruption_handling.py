```python
from twilio.rest import Client
from eleven_labs_api import ElevenLabsAPI
from call_handling import CallHandler
from latency_management import LatencyManager

class InterruptionHandler:
    def __init__(self, twilio_client: Client, eleven_labs_api: ElevenLabsAPI, call_handler: CallHandler, latency_manager: LatencyManager):
        self.twilio_client = twilio_client
        self.eleven_labs_api = eleven_labs_api
        self.call_handler = call_handler
        self.latency_manager = latency_manager

    def detect_interruption(self, call_id: str):
        call_data = self.call_handler.get_call_data(call_id)
        if call_data['status'] == 'interrupted':
            return True
        return False

    def handle_interruption(self, call_id: str):
        if self.detect_interruption(call_id):
            self.call_handler.pause_call(call_id)
            self.latency_manager.reduce_latency(call_id)
            self.call_handler.resume_call(call_id)

    def resume_call_after_interruption(self, call_id: str):
        if self.detect_interruption(call_id):
            self.call_handler.resume_call(call_id)
            self.eleven_labs_api.send_message('Call resumed after interruption', call_id)
```