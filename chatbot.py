import random

# Lists of greetings, questions, and responses
greetings = ["hello", "hi", "hey", "howdy", "greetings"]
responses_to_greetings = ["Hello!", "Hi there!", "Hey!", "How can I assist you?", "Greetings!"]

questions = ["how are you", "what's your name", "who are you", "what can you do"]
responses_to_questions = [
    "I'm just a chatbot, but I'm here to help.",
    "I don't have a name, but you can call me ChatBot.",
    "I'm a chatbot created by OpenAI.",
    "I can answer questions and have conversations with you.",
]

farewells = ["goodbye", "bye", "see you", "later"]
responses_to_farewells = ["Goodbye!", "See you later!", "Farewell!", "Have a great day!"]

# Dictionary of additional responses for specific keywords or phrases
custom_responses = {
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Sure, here's a joke: What do you call a fish with no eyes? Fsh!"],
    "how's the weather": ["I'm sorry, I don't have real-time weather information. You can check a weather website or app for that."],
    "thanks": ["You're welcome!", "No problem.", "Anytime!"],
}

# Decision-making responses
decisions = ["should I do this", "what do you recommend", "help me decide"]
decision_responses = ["It depends on the specific situation. Can you provide more details?", "I need more information to give a recommendation."]

# Knowledge base with basic facts
knowledge_base = {
    "capital of france": "The capital of France is Paris.",
    "largest planet": "The largest planet in our solar system is Jupiter.",
    "color of the sky": "The sky appears blue during the day due to Rayleigh scattering.",
}

# Main chatbot loop
print("ChatBot: Hello! I'm your friendly chatbot. You can start a conversation or ask me anything. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ").lower()

    if user_input == 'exit':
        print("ChatBot: Goodbye!")
        break

    bot_response = None

    if user_input in greetings:
        bot_response = random.choice(responses_to_greetings)
    elif any(question in user_input for question in questions):
        bot_response = random.choice(responses_to_questions)
    elif user_input in farewells:
        bot_response = random.choice(responses_to_farewells)
    elif user_input in custom_responses:
        bot_response = random.choice(custom_responses[user_input])
    elif any(decision in user_input for decision in decisions):
        bot_response = random.choice(decision_responses)
    else:
        for keyword, response in knowledge_base.items():
            if keyword in user_input:
                bot_response = response
                break

    if bot_response is None:
        bot_response = "I'm sorry, I don't understand. Could you please rephrase your question or statement?"

    print("ChatBot: " + bot_response)
