import nltk
import random
import string

# Sample data for chatbot responses
GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up", "hey"]
GREETING_RESPONSES = ["hi", "hey", "hello", "I am glad you are talking to me"]

# Sample corpus for chatbot responses
CORPUS = """
Hello! How can I help you?
I am an AI chatbot created to assist you.
You can ask me about various topics.
I can answer questions about weather, news, and more.
Feel free to ask me anything!
"""

def preprocess_text(text):
    return nltk.word_tokenize(text.lower())

def generate_response(user_input):
    # Check for greetings
    for word in user_input.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
    
    # Fallback response if no match found
    return "I'm sorry, I don't understand. Can you rephrase?"

def chatbot():
    print("Hi! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == 'bye':
            print("Chatbot: Bye! Have a nice day.")
            break
        
        response = generate_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    nltk.download('punkt')  # Ensure necessary NLTK data is downloaded
    chatbot()
