"""
EVA - Enhanced Virtual Assistant

Version: 2.0
Author: Firas Ouali

EVA is a virtual assistant that interacts with users through voice commands. It can provide information
about time, date, weather, news, play songs from YouTube, search Wikipedia, and answer general knowledge questions
using WolframAlpha.

Copyright (c) 2022 Firas Ouali. All Rights Reserved.
"""

import os
import tempfile
import datetime
import wikipediaapi
import wolframalpha
import requests
import pygame
import webbrowser
import psutil
import speech_recognition as sr
from gtts import gTTS

# Replace these with your API keys
wolframalpha_api_key = "YOUR_WOLFRAMALPHA_API_KEY"
openweathermap_api_key = "YOUR_OPENWEATHERMAP_API_KEY"
currents_api_key = "YOUR_NEWSAPI_KEY"

# Initialize Pygame mixer
pygame.mixer.init()

# Convert text to speech and play using pygame
def speak(text):
    sound = gTTS(text, lang='en')
    temp_file_path = tempfile.mktemp(suffix='.mp3')
    sound.save(temp_file_path)
    pygame.mixer.music.load(temp_file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Check every 10 milliseconds
    try:
        os.remove(temp_file_path)  # Remove temp file after playback
    except PermissionError:
        print(f"PermissionError: Could not delete file {temp_file_path}")

# Introduce the assistant
def introduce():
    introduction = "Hello, I am EVA, your personal AI assistant."
    speak(introduction)
    print(introduction)

# Provide the current time
def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")
    print(f"The current time is {current_time}")

# Provide the current date
def get_date():
    current_date = datetime.date.today().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")
    print(f"Today's date is {current_date}")

# Search Wikipedia and read the summary
def search_wikipedia(query):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(query)
    if page.exists():
        speak(f"According to Wikipedia: {page.summary[:500]}")  # Limit to 500 characters for speech
        print(page.summary[:500])
    else:
        speak("I could not find any information on that topic.")
        print("No results found on Wikipedia.")

# Answer questions using WolframAlpha
def ask_wolframalpha(query):
    client = wolframalpha.Client(wolframalpha_api_key)
    try:
        res = client.query(query, params={'format': 'plaintext'})  # Use 'plaintext' for short answers
        if res.results:
            answer = next(res.results).text
            speak(answer)  # Speak the answer
            print(answer)  # Print the answer to console
        else:
            speak("I could not find an answer to that question.")
            print("No results from WolframAlpha.")
    except (StopIteration, ValueError) as e:
        speak("I could not find an answer to that question.")
        print(f"Error querying WolframAlpha: {e}")

# Open a website
def open_website(url):
    speak(f"Opening {url}")
    webbrowser.open(url)
    print(f"Opening {url}")

# Get system status (CPU and memory usage)
def get_system_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    speak(f"Current CPU usage is at {cpu_usage} percent.")
    speak(f"Current memory usage is at {memory_info.percent} percent.")
    print(f"Current CPU usage: {cpu_usage}%")
    print(f"Current memory usage: {memory_info.percent}%")

# Play a song
def play_song(song_name):
    speak(f"Playing {song_name} on YouTube")
    query = song_name.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    print(f"Playing {song_name} on YouTube")

# Get the weather
def get_weather(city):
    api_key = openweathermap_api_key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]
        weather_report = f"The temperature in {city} is {temperature} degrees Celsius with {description} and humidity of {humidity} percent."
        speak(weather_report)
        print(weather_report)
    else:
        speak("City not found.")
        print("City not found.")

# Get top news headlines
def get_news():
    api_key = currents_api_key
    base_url = f"https://api.currentsapi.services/v1/latest-news?apiKey={api_key}"
    response = requests.get(base_url)
    data = response.json()
    if data["status"] == "ok":
        articles = data["news"][:5]
        news_report = "Here are the top 5 news headlines: "
        for i, article in enumerate(articles, 1):
            news_report += f"{i}. {article['title']}. "
        speak(news_report)
        print(news_report)
    else:
        speak("Unable to fetch news at the moment.")
        print("Unable to fetch news.")

# Recognize speech input from the microphone using Google's Speech Recognition
def recognize_speech():
    """
    Recognizes speech input from the microphone using Google's Speech Recognition.
    
    Returns:
    - str: The recognized text from speech.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening... Speak something:")
        audio = recognizer.listen(mic)
    
    try:
        text = recognizer.recognize_google(audio, language='en')
        return text.lower()
    except sr.UnknownValueError:
        return "Sorry, I could not understand what you said."
    except sr.RequestError:
        return "Sorry, I am unable to process your request at the moment."

# Handle user requests
def handle_request(request):
    if "time" in request:
        get_time()
    elif "date" in request:
        get_date()
    elif "wikipedia" in request:
        query = request.replace("wikipedia", "").strip()
        search_wikipedia(query)
    elif "open" in request and "website" in request:
        url = request.replace("open website", "").strip()
        open_website(url)
    elif "cpu" in request or "system" in request:
        get_system_status()
    elif "who are you" in request or "introduce yourself" in request:
        introduce()
    elif "play" in request and "song" in request:
        song_name = request.replace("play song", "").strip()
        play_song(song_name)
    elif "weather" in request:
        city = request.replace("weather", "").strip()
        get_weather(city)
    elif "news" in request:
        get_news()
    elif "exit" in request:
        speak("Goodbye!")
        exit()
    else:
        ask_wolframalpha(request)

# Main function to run the assistant
def main():
    while True:
        try:
            print("\nSay 'Hey EVA' to start interaction or 'exit' to quit:")
            user_input = recognize_speech()
            print(f"You said: {user_input}")
            if user_input.lower() == "exit":
                speak("Goodbye!")
                break
            # Check if user starts with the wake word "Hey EVA"
            if user_input.lower().startswith("hey eva"):
                introduce()
                handle_request(user_input[len("hey eva"):].strip())
            else:
                print("Please start with 'Hey EVA' to interact.")
        except KeyboardInterrupt:
            print("\nExiting program...")
            break

if __name__ == "__main__":
    main()
