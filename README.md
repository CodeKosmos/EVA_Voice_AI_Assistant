# EVA_Voice_AI_Assistant
#EVA: Enhanced Virtual Assistant <br />
#EVA (Enhanced Virtual Assistant) is a Python-based program designed to provide voice interaction, information retrieval, and system management functionalities using various APIs and modules. <br />

Features:

Voice Interaction<br />
EVA can recognize speech input and respond with synthesized voice output using Google Text-to-Speech (gTTS) and pyttsx3.<br />

Information Retrieval
EVA can fetch various types of information and perform tasks such as:<br />
    - Time and Date: Provides the current time and date on request.<br />
    - Wikipedia: Fetches information from Wikipedia using the wikipedia-api.<br />
    - WolframAlpha: Answers questions and provides computations using the WolframAlpha API (wolframalpha).<br />
    - Weather: Retrieves current weather conditions and forecasts using the OpenWeatherMap API.<br />
    - News: Fetches the latest news headlines using the NewsAPI.<br />
    - System Status: Provides system information such as CPU usage, memory usage, and disk space using psutil.<br />
						
System Management<br />
EVA can perform system management tasks such as:<br />
   
    - CPU and Memory: Reports current CPU usage and memory usage.<br />
    - Play Music: Plays music from YouTube based on user requests.<br />

Getting Started<br />
Prerequisites<br />
Ensure you have Python 3 installed. You can download Python from python.org.<br />

Installation<br />
Clone the repository:<br />
git clone<br />
https://github.com/CodeKosmos/EVA_Voice_AI_Assistant.git<br />

cd your_repository<br />

Install required Python modules using pip:<br />

pip install -r requirements <br />

This will install the following modules:<br />
gtts - Google Text-to-Speech<br />
pyttsx3 - Text-to-Speech library<br />
wikipedia-api - Wikipedia API wrapper<br />
wolframalpha - WolframAlpha API client<br />
psutil - System and process utilities<br />

API Keys<br />
To use EVA effectively, you need API keys for the following services:<br />
    - WolframAlpha API: Obtain your API key from the WolframAlpha Developer Portal.<br />
    - OpenWeatherMap API: Get your API key from OpenWeatherMap API.<br />
    - NewsAPI: Sign up for an API key at NewsAPI.<br />
Ensure you replace placeholders in the code (YOUR_WOLFRAMALPHA_API_KEY, YOUR_OPENWEATHERMAP_API_KEY, YOUR_NEWSAPI_KEY) with your actual API keys.<br />

Usage<br />
Run the main Python script to start EVA:<br />
python main.py<br />

Example Commands<br />
You can interact with EVA using voice commands such as:<br />

"Hey Eva, What time is it?"<br />
"Hey Eva, Tell me about Python programming"<br />
"Hey Eva, How is the weather in Berlin?"<br />
"Hey Eva, Give me the latest news"<br />

How It Works:<br />
EVA listens for voice commands using the microphone. When it hears the wake word "Hey EVA", it processes the command using speech recognition (speech_recognition library). Depending on the command, it fetches information from Wikipedia, WolframAlpha, or other APIs. EVA can also perform system management tasks like reporting CPU usage and playing songs from YouTube.<br />

Acknowledgments<br />
Thanks to the developers of gtts, pyttsx3, wikipedia-api, wolframalpha, psutil, and other libraries used in this project.
