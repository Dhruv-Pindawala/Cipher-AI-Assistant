import pyttsx3 # text-to-speech module

engine = pyttsx3.init() # initialisation

def speak(message):
    engine.say(message)
    engine.runAndWait()

speak("hey fellas,how may i help you?")