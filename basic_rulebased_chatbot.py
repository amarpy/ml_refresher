#basic_rulebased_chatbot

import re

#a dictionary that maps keywords to predefined responses

responses = {
    "hello" : "Hi there! How may I assist?",
    "hi" : "Hello! How may I help?",
    "how are you?" : "I'm just a bot. But, I'm doing great. How may I help you?",
    "what is your name?" : "I'm just a bot created to assist you. How mau I assist?",
    "help" : "Sure. What do you need help with?",
    "bye" : "Goodbye!",
    "thank you" : "you're welcome! Happy to help.",
    "default" : "I'm not sure I understand. Would you please rephrase?"
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    for keyword in responses:
        if re.search(keyword, user_input):
            return responses[keyword]
    
    return responses["default"]

def chatbot():
    print("Chatbot: Hello! I'm here to assist you. (type 'bye' to exit)")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Goodbye!")
            break

        response = chatbot_response(user_input)

        print(f"Chatbot: {response}")

chatbot()