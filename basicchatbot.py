def get_response(message):
    message = message.lower()

    if "hello" in message:
        return "Hi!"
    elif "how are you" in message:
        return "I'm fine, thanks!"
    elif "bye" in message:
        return "Goodbye!"
    else:
        return "I don't understand."

def chat():
    print("🤖 Chatbot is active. Type 'bye' to end.\n")
    while True:
        user = input("You: ")
        response = get_response(user)
        print("Bot:", response)
        if "bye" in user.lower():
            break

# Start chat
chat()