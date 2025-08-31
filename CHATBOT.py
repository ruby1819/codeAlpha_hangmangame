

def chatbot():
    print("Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi"]:
            print("Chatbot: Hi! How can I help you?")
        elif user_input in ["how are you", "how are you?"]:
            print("Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")
        elif user_input in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        elif user_input in ["thanks", "thank you"]:
            print("Chatbot: You're welcome!")
        else:
            print("Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()