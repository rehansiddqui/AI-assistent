import speech_recognition as sr
import pyaudio
import webbrowser
import pyttsx3
import veriable
import requests
import time

# the name of the assistance with which it can be wake up
assistantName = "jarvis"


# confighuring ai
def ai(command):
   # Replace these values with your actual data
   OPENROUTER_API_KEY = veriable.ai_api

   response = requests.post(
      url="https://openrouter.ai/api/v1/chat/completions",
      headers={
         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
         "Content-Type": "application/json"
      },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": f"You are a virtual assistant named {assistantName} skilled in general tasks like Alexa and Google Cloud. Give short responses please you speak in hindi and you are very frank"},
                    {"role": "user", "content": command}
                ]
            }
        )

   # Check response status
   if response.status_code == 200:
      result = response.json()
      print (result['choices'][0]['message']['content'])
      return result['choices'][0]['message']['content']
   else:
      print(f"Error: {response.status_code}, {response.text}")

# fetching newss

# Define the News API URL with your API key
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=' + veriable.news_api

# Function to fetch and return news headlines
def fetch_and_speak_news():
    # Fetch the latest news headlines
    response = requests.get(NEWS_API_URL)
    news_data = response.json()
    
    if news_data['status'] == 'ok':
        articles = news_data['articles']
        headlines = [article['title'] for article in articles[:5]]  # Get top 5 headlines
        
        # Speak the headlines
        for idx, headline in enumerate(headlines, 1):
            speak(f"Title {idx}")
            speak(headline)
            time.sleep(1)  # Pause for 1 second between headlines
            
        return headlines  # Return headlines if you want to do something else with them
    else:
        error_message = "Unable to fetch news at the moment."
        speak(error_message)
        return [error_message]


def speak(text):
  engine.say(text)
  engine.runAndWait()

engine = pyttsx3.init()
r = sr.Recognizer()
def liten_command(command):
   # opning diffrent web and playing songs
   if "open google" in command.lower():
      webbrowser.open("https://google.com")
      speak("opning")
   elif "open facebook" in command.lower():
      webbrowser.open("https://facebook.com")
      speak("opning")
   elif "open youtube" in command.lower():
      webbrowser.open("https://youtube.com")
      speak("opning")
   elif "open linkdin" in command.lower():
      webbrowser.open("https://linkdin.com")
      speak("opning")
   elif command.lower().startswith("play"):
        # Remove "play " from the command to get the song name
        song_name = command.lower().replace("play ", "", 1).strip()
        link = veriable.songs.get(song_name)
        webbrowser.open(link)
        speak("playing")
      #speaking news
   elif "news" in command.lower():
      fetch_and_speak_news()
      #letting ai handel

   elif "weather" in command.lower():
      ipinfo_url = "http://ipinfo.io"
      location_data = requests.get(ipinfo_url).json()
      loc = location_data['loc'].split(',')
      latitude = loc[0]
      longitude = loc[1]

      # Step 2: Use OpenWeatherMap API to get weather data
      weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={veriable.weather_api}&units=metric"

      weather_data = requests.get(weather_url).json()

      # Step 3: Print the current weather
      if weather_data['cod'] == 200:
         location = weather_data['name']
         temp = weather_data['main']['temp']
         weather_desc = weather_data['weather'][0]['description']
         speak(f"Location: {location}")
         print(f"Location: {location}")
         speak(f"Temperature: {temp}°C")
         print(f"Temperature: {temp}°C")
         speak(f"Weather: {weather_desc}")
         print(f"Weather: {weather_desc}")
      else:
         speak(f"Error: {weather_data['message']}")
         print(f"Error: {weather_data['message']}")
      
   else:
      openrouter = ai(command)
      speak(openrouter)

   


if (__name__ == "__main__"):
    speak(f"initializing {assistantName}....")
    while True:
      try:
        with sr.Microphone() as source:
          print("listening.....")
          audio = r.listen(source,timeout=3,phrase_time_limit=0)
         #  audio = r.listen(source)
          wake_word = (r.recognize_google(audio))
          print(wake_word)
          if(wake_word.lower() == assistantName):
             speak("yes sir")
             with sr.Microphone() as source:
                audio = r.listen(source)
                command = r.recognize_google(audio)
                liten_command(command)
      except Exception as e:
         print(f"error:{e}")