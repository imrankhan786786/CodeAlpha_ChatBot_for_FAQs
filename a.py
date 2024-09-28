import nltk
from nltk.chat.util import Chat, reflections

# Predefined FAQs and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! How can I help?"]
    ],
    [
        r"what is your name?",
        ["I am an FAQ chatbot. You can ask me questions about this service.",]
    ],
    [
        r"how does this service work?",
        ["This service allows you to ask common questions, and I will provide answers based on a predefined set of FAQs.",]
    ],
    [
        r"how can i (.*)?",
        ["You can %1 by following these steps: ...",]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "Glad to help!"]
    ],
    [
        r"quit|exit",
        ["Goodbye! Have a nice day!"]
    ],
]

# Function to start chatbot
def faq_chatbot():
    print("FAQ Chatbot: Hello! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Start the chatbot
if __name__ == "__main__":
    faq_chatbot()