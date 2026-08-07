import random
import string
from datetime import datetime

INTENTS = {
    "greeting": {
        "keywords": ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"],
        "responses": [
            "Hello! How can I help you today?",
            "Hi! Nice to meet you.",
            "Hello! What can I do for you?"
        ]
    },

    "farewell": {
        "keywords": ["bye", "goodbye", "see you", "exit", "quit"],
        "responses": [
            "Goodbye! Have a wonderful day.",
            "See you again!",
            "Bye! Take care."
        ]
    },

    "thanks": {
        "keywords": ["thanks", "thank you", "thx"],
        "responses": [
            "You're welcome!",
            "Happy to help!",
            "Anytime!"
        ]
    },

    "name": {
        "keywords": ["your name", "who are you"],
        "responses": [
            "I am a Python AI Chatbot developed using rule-based NLP."
        ]
    },

    "python": {
        "keywords": ["python"],
        "responses": [
            "Python is a powerful programming language used for AI, web development, and automation."
        ]
    },

    "ai": {
        "keywords": ["ai", "artificial intelligence", "machine learning"],
        "responses": [
            "Artificial Intelligence enables machines to perform tasks that normally require human intelligence."
        ]
    },

    "weather": {
        "keywords": ["weather", "temperature", "rain"],
        "responses": [
            "I cannot access live weather information."
        ]
    },

    "help": {
        "keywords": ["help", "support"],
        "responses": [
            "You can ask me about AI, Python, weather, or say hello."
        ]
    }
}


def preprocess(text):
    text = text.lower()

    for p in string.punctuation:
        text = text.replace(p, "")

    return text.split()


def recognize_intent(text):
    words = preprocess(text)

    best = None
    score = 0

    for intent, data in INTENTS.items():
        current = 0

        for keyword in data["keywords"]:
            keyword_words = keyword.split()

            if all(word in words for word in keyword_words):
                current += 1

        if current > score:
            score = current
            best = intent

    return best


class ChatBot:

    def __init__(self):
        self.name = None

    def chat(self, message):

        if message.lower().startswith("my name is"):
            self.name = message[11:].strip().title()
            return f"Nice to meet you, {self.name}!"

        if "time" in message.lower():
            return "Current Time: " + datetime.now().strftime("%I:%M %p")

        intent = recognize_intent(message)

        if intent is None:
            return "Sorry, I didn't understand. Type 'help'."

        response = random.choice(INTENTS[intent]["responses"])

        if self.name:
            response = f"{self.name}, {response}"

        return response


print("="*50)
print("AI CHATBOT APPLICATION")
print("="*50)

bot = ChatBot()

while True:

    user = input("You: ")

    if user.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    print("Bot:", bot.chat(user))