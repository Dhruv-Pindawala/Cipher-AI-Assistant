import pyttsx3 # text-to-speech module

engine = pyttsx3.init() # initialisation
# voice selection
voices = engine.getProperty('voices') # obtain voice properties from the module
engine.setProperty('voice', voices[1].id) # [1] for female voice and [0] for male voice. 0 to 5, total 6 different voices.
# speed selection
newVoiceRate = 140 # words per minute
engine.setProperty('rate', newVoiceRate)


def speak(message):
    engine.say(message)
    engine.runAndWait()

speak('hello there')