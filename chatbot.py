import random
from datetime import datetime

def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hi", "hello", "hey"]
    jokes = [
        "Why don’t programmers like nature? Too many bugs 🐛",
        "Why did the computer go to the doctor? Because it caught a virus 🤒",
        "Why do Java developers wear glasses? Because they don’t C 👓"
    ]

    if any(word in user_input for word in greetings):
        return "Hello! 😊 How can I help you today?"

    elif "your name" in user_input:
        return "I'm a simple chatbot built using Python and Streamlit."

    elif "time" in user_input:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"

    elif "joke" in user_input:
        return random.choice(jokes)

    elif "help" in user_input:
        return "You can ask me greetings, time, jokes, or simple questions."

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day 👋"

    else:
        return "Sorry, I didn’t understand that. Can you try something else?"
