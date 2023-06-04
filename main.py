import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
	tts = gTTS(text = text, lang="en")
	filename = "voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		input = ""

		try:
			# use Google API to recognize what we say
			input = r.recognize_google(audio)
			# prints the input given by the microphone
			print(input)
		except Exception as e:
			# otherwise prints the exception
			print("Exception" + str(e))

	return input

speak("Hello there")

text = get_audio()

if "hello" in text:
	speak("hello, how are you?")