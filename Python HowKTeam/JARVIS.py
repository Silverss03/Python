from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
recognizer = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty('rate',150)
todo_list = []
def some_function():
	print("Hello World!")
mappings = {'greeting':some_function}	

assistant = GenericAssistant('intents.json',intent_methods=mappings)
assistant.train_model()
assistant.request("")


{"intents":[
{"tag": "".
"patterns":[""],
"responses" : [""]}
]}