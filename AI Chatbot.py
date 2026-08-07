print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! How can I help you?")
    elif "how are you" in user:
        print("Bot: I'm doing great! 😊")
    elif "your name" in user:
        print("Bot: I'm a simple AI chatbot.")
    elif "bye" in user:
        print("Bot: Goodbye! 👋")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")