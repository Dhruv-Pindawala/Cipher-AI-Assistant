import pyttsx3 # text-to-speech module
import datetime
import speech_recognition as sr # for speech recognition, to take commands through speech, requires internet

engine = pyttsx3.init() # initialisation
# voice selection
voices = engine.getProperty('voices') # obtain voice properties from the module
engine.setProperty('voice', voices[1].id) # [1] for female voice and [0] for male voice. 0 to 5, total 6 different voices.
# speed selection
newVoiceRate = 150 # words per minute
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

def wishme():
    hour = datetime.datetime.now().hour

    if 6<=hour<12:
        speak('Good morning sir!')
    elif 12<=hour<18:
        speak('Good afternoon sir!')
    elif 18<=hour<20:
        speak('Good evening sir!')
    else:
        speak('Good night sir!')

    speak('Cipher is always at your service. How may I help you? But before that, let me share with you the present time and date.')
    date()
    time()

def takeCommand():
    r = sr.Recognizer() # initialization
    with sr.Microphone() as source: # defining mic as a source for commands
        print('Listening....')
        r.pause_threshold = 1 # waits for 1 second before it starts listening
        audio = r.listen(source)
    
    try:
        print('Recognizing....')
        query = r.recognize_google(audio, 'en=IN')
        print(query)
    except Exception as e:
        print(e)
        speak('Unable to recognize your command. Please say it again!')
        return "None"
    
    return query

takeCommand()
