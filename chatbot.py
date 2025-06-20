def get_bot_response(user_input):
    """
    Returns a predefined response based on the user's input.
    """
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        return "Hi there! How can I assist you today?"

    # Well-being
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm just a bunch of code, but I'm running great! 😊"

    # Bot identity
    elif user_input in ["what's your name", "who are you"]:
        return "I'm your friendly chatbot, here to help!"

    # Help options
    elif user_input in ["what can you do", "help"]:
        return "I can chat with you, tell the date and time, share jokes, and more!"

    # Time and date
    elif user_input in ["what's the time", "time please", "current time"]:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%I:%M %p')}."

    elif user_input in ["what's the date", "today's date", "date please"]:
        from datetime import datetime
        return f"Today's date is {datetime.now().strftime('%B %d, %Y')}."

    # Gratitude
    elif user_input in ["thank you", "thanks"]:
        return "You're welcome! Let me know if I can help with anything else. 😊"

    # Goodbye
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a wonderful day ahead! 👋"

    # Jokes
    elif user_input in ["tell me a joke", "joke", "make me laugh"]:
        return "Why don't programmers like nature? It has too many bugs. 😄"

    # Weather (basic reply)
    elif user_input in ["what's the weather", "weather today"]:
        return "I'm not connected to live weather data, but I hope it's sunny wherever you are! ☀️"

    # AI understanding
    elif user_input in ["are you real", "are you human"]:
        return "I'm an AI-powered chatbot, not human, but I'm here to help like one!"

    # Mood
    elif user_input in ["i am sad", "feeling low", "not good"]:
        return "I'm sorry to hear that. Remember, tough times don't last — you're stronger than you think. 💪"

    elif user_input in ["i am happy", "feeling good", "i'm great"]:
        return "That's wonderful to hear! Keep spreading the positive vibes! 😄"

    else:
        return "I'm not sure how to respond to that. Try asking something else or type 'help' to see what I can do."

def start_chat():
    """
    Starts the chatbot loop.
    """
    print("🤖 Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.\n")

    while True:
        user_message = input("🧑 You: ")
        response = get_bot_response(user_message)
        print("🤖 Chatbot:", response)

        if user_message.lower().strip() in ["bye", "goodbye", "see you"]:
            break

if __name__ == "__main__":
    start_chat()