def get_predefined_response(user_message):
    # Define your logic for generating predefined responses based on user messages
    if user_message.lower() == 'hi':
        return "Hello there! How can I help you?"
    elif user_message.lower() == 'hello':
        return "Hi! What can I do for you today?"
    elif user_message.lower() == 'bye':
        return "Goodbye! Have a great day!"
    elif user_message.lower() == 'pleasure to meet you':
        return "The pleasure is mine! How may I assist you?"
    elif user_message.lower() == 'good evening':
        return "Good evening! What brings you here?"
    elif user_message.lower() == 'thank you':
        return "You're welcome! If you have any more questions, feel free to ask."
    else:
        # Default response if the message doesn't match any predefined ones
        return "I'm not sure how to respond to that. Feel free to ask me anything else!"