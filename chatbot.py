import json

def load_intents():
    with open('intents.json') as file:
        data = json.load(file)
    return data

import re

def preprocess_input(user_input):
    # Convert to lowercase
    user_input = user_input.lower()

    # Remove punctuation
    user_input = re.sub(r'[^\w\s]', '', user_input)

    # Tokenize words
    user_input = user_input.split()

    return user_input

def get_response(intents_data, user_input):
    preprocessed_input = preprocess_input(user_input)

    # Calculate similarity between user input and intent patterns
    max_similarity = 0
    matched_intent = None

    for intent in intents_data['intents']:
        similarity = 0
        for pattern in intent['patterns']:
            pattern_tokens = preprocess_input(pattern)
            similarity += len(set(preprocessed_input) & set(pattern_tokens))
        similarity /= len(intent['patterns'])

        if similarity > max_similarity:
            max_similarity = similarity
            matched_intent = intent

    # Generate a response based on the matched intentme
    if matched_intent:
        responses = matched_intent['responses']
        return responses[0]
    else:
        return "I'm sorry, I didn't understand that."
    
    
def chatbot_interface():
    print("Welcome to the basic chatbot!")
    intents_data = load_intents()

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            break
        response = get_response(intents_data, user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot_interface()