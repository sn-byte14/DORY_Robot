import speech_recognition as sr
import pyttsx3
import aiml
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

# Initialize Sentiment Analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

# Load AIML-based Chatbot
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML")

def speak(text):
    """Function to make Dory speak"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to recognize speech input"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Could not request results."

def analyze_sentiment(text):
    """Function to analyze sentiment"""
    sentiment_score = sentiment_analyzer.polarity_scores(text)
    if sentiment_score['compound'] >= 0.05:
        return "Positive"
    elif sentiment_score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def dory_chat():
    """Main chatbot function"""
    while True:
        user_input = listen()
        if user_input.lower() in ["exit", "quit", "bye"]:
            speak("Goodbye! Have a great day!")
            break
        
        sentiment = analyze_sentiment(user_input)
        print(f"Sentiment: {sentiment}")
        
        response = kernel.respond(user_input)
        speak(response)

# Start Dory Chatbot
if _name_ == "_main_":
    speak("Hello! I am Dory. How can I help you today?")
    dory_chat()
