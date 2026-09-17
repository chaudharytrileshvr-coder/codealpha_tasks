def get_bot_reply(user_input):
  
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks! How about you?"
    elif "your name" in user_input:
        return "I'm a simple rule-based chatbot created in Python."
    elif "help" in user_input:
        return "I can chat with you! Try saying hello, how are you, bye."
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Can you say it differently?"

def start_chatbot():
    print("--- Basic Chatbot ---")
    print("Bot: Hello! Type 'bye' to exit.")

    while True:
        user_msg = input("You: ")
        
        reply = get_bot_reply(user_msg)
        print(f"Bot: {reply}")

      
        if "bye" in user_msg.lower() or "exit" in user_msg.lower() or "quit" in user_msg.lower():
            break


start_chatbot()