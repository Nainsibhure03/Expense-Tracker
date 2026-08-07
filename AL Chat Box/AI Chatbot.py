import random
import re
import datetime


# Dictionary Based Intent Recognition
intents = {

    "greeting": {
        "keywords": ["hello", "hi", "hey", "hii"],
        "responses": [
            "Hello! How can I help you?",
            "Hi! Nice to meet you.",
            "Hey! What can I do for you?"
        ]
    },

    "name": {
        "keywords": ["your name", "who are you"],
        "responses": [
            "I am an AI chatbot created using Python.",
            "I am your virtual assistant."
        ]
    },

    "python": {
        "keywords": ["python", "coding", "programming"],
        "responses": [
            "Python is a powerful programming language used in AI, Data Science and Web Development.",
            "Python is one of the most popular languages for beginners and professionals."
        ]
    },

    "ai": {
        "keywords": ["ai", "artificial intelligence", "machine learning"],
        "responses": [
            "Artificial Intelligence allows machines to think and learn like humans.",
            "AI is used in chatbots, automation and intelligent systems."
        ]
    },

    "time": {
        "keywords": ["time", "current time"],
        "responses": [
            "Current time is " + datetime.datetime.now().strftime("%I:%M %p")
        ]
    },

    "thanks": {
        "keywords": ["thank", "thanks"],
        "responses": [
            "You're welcome!",
            "Glad I could help."
        ]
    },

    "bye": {
        "keywords": ["bye", "exit", "quit"],
        "responses": [
            "Goodbye! Have a great day.",
            "See you soon!"
        ]
    }
}



# Text Cleaning Function
def preprocess(text):
    text = text.lower()
    text = re.sub("[^a-zA-Z0-9 ]", "", text)
    return text



# Intent Detection Function
def detect_intent(user_input):

    user_input = preprocess(user_input)

    for intent, data in intents.items():

        for keyword in data["keywords"]:

            if keyword in user_input:
                return intent

    return "unknown"



# Generate Response
def chatbot_response(intent):

    if intent in intents:
        return random.choice(intents[intent]["responses"])

    return "Sorry, I don't understand. Please try another question."



# Main Chatbot Program

print("--------------------------------")
print("      AI CHATBOT USING PYTHON")
print("--------------------------------")
print("Type 'bye' to close chatbot\n")


while True:

    user = input("You: ")

    intent = detect_intent(user)

    reply = chatbot_response(intent)

    print("Bot:", reply)


    if intent == "bye":
        break