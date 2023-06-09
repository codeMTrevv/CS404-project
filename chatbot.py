import nltk
from nltk.chat.util import Chat, reflections

#welcome statement that prints at the beginning of the program
print("Welcome! How may I assist you today?")

#dictionary to capture and match the user input
pairs = [
    [
        r"(?:(.*)) name is (?:(.*))?",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!"]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you.", "I'm fine, thanks."]
    ],
    [
        r"quit",
        ["Bye for now!", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand what you said. Please try again.",]
    ]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
