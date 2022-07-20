import pyttsx3
import speech_recognition

engine = pyttsx3.init()
recognizer = speech_recognition.Recognizer()

def speak(message):
	print(message)
	engine.say(message)
	engine.runAndWait()


def listen():
	print('listening...')
	with speech_recognition.Microphone() as mic:
		try:
			recognizer.adjust_for_ambient_noise(mic, duration=1)
			audio = recognizer.listen(mic)
			text = recognizer.recognize_google(audio)
			print(text)
			return text
		except speech_recognition.UnknownValueError as e:
			return "Sorry, I don't understand what you jus said"