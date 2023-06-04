import os
import time
import pygame
import speech_recognition as sr
from gtts import gTTS

def speak(text):
	pygame.init()
	pygame.mixer.music.load("voice.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		continue
	pygame.quit()

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

