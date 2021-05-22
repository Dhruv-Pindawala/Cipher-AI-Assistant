import pyttsx3 # text-to-speech module
import datetime

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

def time():
    Time = datetime.datetime.now().strftime("%I:%p:%M 'minutes and' %S 'seconds")
    speak('The present time is {}'.format(Time))

def date():
    year = str(datetime.datetime.now().year)
    m = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = m[int(datetime.datetime.now().month)]
    date = str(datetime.datetime.now().day)
    speak('Today\'s date is {} {} {}'.format(month,date,year))
