import twilio_setup
import eleven_labs_setup
import call_handling
import latency_management
import interruption_handling
import call_mimic

def main():
    # Initialize Twilio and Eleven Labs
    twilio_api = twilio_setup.initialize_twilio()
    eleven_labs_api = eleven_labs_setup.initialize_eleven_labs()

    # Start a call
    call_data = call_handling.initiate_call(twilio_api, eleven_labs_api)

    # Monitor the call for latency and interruptions
    while call_data['status'] != 'ended':
        latency = latency_management.measure_latency(call_data)
        if latency > 0:
            latency_management.reduce_latency(call_data, latency)

        if interruption_handling.detect_interruption(call_data):
            interruption_handling.handle_interruption(call_data)

        # Mimic real call
        call_mimic.simulate_background_noise(call_data)
        call_mimic.simulate_voice_tones(call_data)

    # End the call
    call_handling.end_call(call_data)

if __name__ == "__main__":
    main()