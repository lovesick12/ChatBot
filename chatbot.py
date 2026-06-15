import json
import random

with open("intents.json") as file:
    data = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                return random.choice(intent["responses"])

    return "Sorry, I couldn't understand your question."