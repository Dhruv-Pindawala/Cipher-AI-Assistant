import pyttsx3 # text-to-speech module
import datetime
import speech_recognition as sr # for speech recognition, to take commands through speech, requires internet
import wikipedia
import webbrowser as wb
import os
import pyautogui # for screenshots
import psutil # cpu and batery updates
import pyjokes # for jokes
from urllib.request import urlopen
import json
import requests

engine = pyttsx3.init() # initialisation
# voice selection
voices = engine.getProperty('voices') # obtain voice properties from the module
engine.setProperty('voice', voices[1].id) # [1] for female voice and [0] for male voice. 0 to 5, total 6 different voices.
# speed selection
newVoiceRate = 155 # words per minute
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

    speak('Cipher is always at your service. How may I help you?')

def takeCommand():
    r = sr.Recognizer() # initialization
    mic = sr.Microphone()
    with mic as source: # defining mic as a source for commands
        r.adjust_for_ambient_noise(source)
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Recognizing....')
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak('Unable to recognize your command. Please say it again!')
        return "None"
    
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save('path including image name')

def cpu():
    usage = str(psutil.cpu_percent)
    speak("currently the cpu is running at {} percent usage".format(usage))

    battery = psutil.sensors_battery
    speak('battery is at', str(battery.percent))

def jokes():
    speak(pyjokes.get_joke())

# main functiion
if __name__=="__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        if 'time' in query: # if asked for time
            time()
        elif 'date' in query: # if asked for date
            date()
        elif 'offline' in query: # to stop our assistant
            quit()
        elif 'wikipedia' in query: # for wiki search
            speak('Searching...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query)
            print(result)
            speak('According to wikipedia')
            speak(result)
        elif 'search' in query: # search using chrome
            speak('What should I search')
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
        elif 'logout' in query:
            os.system('shutdown - 1')
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
        elif 'restart' in query:
            os.system('shutdown /r')
        elif 'play songs' in query:
            songs_dir = '' #path to my local songs folder
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif 'remember' in query:
            speak('what should i remember?')
            data = takeCommand()
            speak('You asked me to remember that', data)
            remember = open('data.txt')
            remember.write(data)
            remember.close()
        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak('You asked me to remember that', remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak('screenshot captured')
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'news' in query:
            try:
                jsonobj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey ={}''').format(os.environ.get('news_api'))
                data = json.load(jsonobj)
                i = 1
                speak("Here are some top news from the times of india")
                for news in data['articles']:
                    speak(str(i) + '.' + news['title'])
                    speak('Description of this news is printed is printed on screen')
                    print(str(i) + '.' + news['title'] + '\n')
                    print(news['description']+'\n')
                    i+=1
            except Exception as e:
                print(str(e))
        elif 'weather' in query:
            api_key = os.environ.get('weather_api')
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak("City name ")
            print("City name : ")
            city_name = takeCommand()
            print(city_name)
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
             
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
            else:
                speak(" City Not Found ")
        