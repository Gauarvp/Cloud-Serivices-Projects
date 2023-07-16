import azure.cognitiveservices.speech as speechsdk

# Set up the speech configuration
speech_key = 'YOUR_SPEECH_KEY'
service_region = ''  # e.g., 'westus'

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Create a speech synthesizer
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Prompt the user to enter the text to be converted to speech
text_to_speak = input("Enter the text to be converted to speech: ")

# Synthesize the speech
result = speech_synthesizer.speak_text_async(text_to_speak).get()

# Save the speech as an audio file
output_file = 'output.mp3'
result.audio.write_to_wave_file(output_file)

print(f'Speech synthesized and saved to "{output_file}"')