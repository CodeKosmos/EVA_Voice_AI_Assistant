# EVA_Voice_AI_Assistant
#EVA: Enhanced Virtual Assistant
#EVA (Enhanced Virtual Assistant) is a Python-based program designed to provide voice interaction, information retrieval, and system management functionalities using various APIs and modules.

Features:

Voice Interaction
EVA can recognize speech input and respond with synthesized voice output using Google Text-to-Speech (gTTS) and pyttsx3.

Information Retrieval
EVA can fetch various types of information and perform tasks such as:
    - Time and Date: Provides the current time and date on request.
    - Wikipedia: Fetches information from Wikipedia using the wikipedia-api.
    - WolframAlpha: Answers questions and provides computations using the WolframAlpha API (wolframalpha).
    - Weather: Retrieves current weather conditions and forecasts using the OpenWeatherMap API.
    - News: Fetches the latest news headlines using the NewsAPI.
    - System Status: Provides system information such as CPU usage, memory usage, and disk space using psutil.

System Management
EVA can perform system management tasks such as:
    - CPU and Memory: Reports current CPU usage and memory usage.
    - Play Music: Plays music from YouTube based on user requests.

Getting Started
Prerequisites
Ensure you have Python 3 installed. You can download Python from python.org.

Installation
Clone the repository:
git clone https://github.com/CodeKosmos/EVA_Voice_AI_Assistant.git
cd your_repository
Install required Python modules using pip:
pip install -r requirements

This will install the following modules:
gtts - Google Text-to-Speech
pyttsx3 - Text-to-Speech library
wikipedia-api - Wikipedia API wrapper
wolframalpha - WolframAlpha API client
psutil - System and process utilities

API Keys
To use EVA effectively, you need API keys for the following services:
    - WolframAlpha API: Obtain your API key from the WolframAlpha Developer Portal.
    - OpenWeatherMap API: Get your API key from OpenWeatherMap API.
    - NewsAPI: Sign up for an API key at NewsAPI.
Ensure you replace placeholders in the code (YOUR_WOLFRAMALPHA_API_KEY, YOUR_OPENWEATHERMAP_API_KEY, YOUR_NEWSAPI_KEY) with your actual API keys.

Usage
Run the main Python script to start EVA:
python main.py

Example Commands
You can interact with EVA using voice commands such as:

"Hey Eva, What time is it?"
"Hey Eva, Tell me about Python programming"
"Hey Eva, How is the weather in Berlin?"
"Hey Eva, Give me the latest news"

How It Works:
EVA listens for voice commands using the microphone. When it hears the wake word "Hey EVA", it processes the command using speech recognition (speech_recognition library). Depending on the command, it fetches information from Wikipedia, WolframAlpha, or other APIs. EVA can also perform system management tasks like reporting CPU usage and playing songs from YouTube.

Acknowledgments
Thanks to the developers of gtts, pyttsx3, wikipedia-api, wolframalpha, psutil, and other libraries used in this project.
