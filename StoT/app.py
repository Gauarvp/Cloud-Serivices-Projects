import asyncio
import azure.cognitiveservices.speech as speechsdk

# Replace 'YOUR_SUBSCRIPTION_KEY' and 'YOUR_REGION' with your actual subscription key and region
speech_key = 'bd9d295fc6934211a3339987b894a96d'
service_region = 'centralindia'

# Configure speech recognition
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

async def recognize_speech():
    print('Speak into your microphone...')
    done = False

    def stop_cb(evt):
        nonlocal done
        print('Speech recognition stopped.')
        done = True

    # Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.recognizing.connect(lambda evt: print('Recognizing:', evt.result.text))
    speech_recognizer.recognized.connect(lambda evt: print('Recognized:', evt.result.text))
    speech_recognizer.session_started.connect(lambda evt: print('Session started.'))
    speech_recognizer.session_stopped.connect(lambda evt: print('Session stopped.'))

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    
    # Wait until speech recognition is stopped
    while not done:
        await asyncio.sleep(0.1)

    # Stop speech recognition
    speech_recognizer.stop_continuous_recognition()
    await speech_recognizer.recognize_once_async()  # Process any remaining speech

async def main():
    await recognize_speech()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
