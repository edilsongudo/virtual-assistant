import speech_recognition

recognizer = speech_recognition.Recognizer()

done = False

while not done:
    print('listening...')
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=1)
        audio = recognizer.listen(mic)
        message = recognizer.recognize_google(audio)
        print(message)