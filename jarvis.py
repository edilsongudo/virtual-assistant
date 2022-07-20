from neuralintents import GenericAssistant
from utils import speak, listen

mappings = {}

assistant = GenericAssistant('intents.json', intent_methods=mappings, model_name="test_model")
# assistant.train_model()
# assistant.save_model()
assistant.load_model()

done = False

while not done:
    try:
        message = listen()

        if message == "stop":
            done = True
            speak('See you later')
        else:
            response = assistant.request(message)
            speak(response)
    except Exception as e:
        speak(str(e))
        print(e)
