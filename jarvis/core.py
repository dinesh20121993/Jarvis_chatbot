import random
import re
from skills.weather import get_weather
from skills.jokes import get_joke
from skills.news import get_news, extract_news_category

def recognize_intent(user_input):
    user_input = user_input.lower()  # Convert to lowercase for easier matching

    if any(word in user_input for word in ["hello", "hi", "hey", "greetings"]):
        return "GREETING"
    elif any(word in user_input for word in ["bye", "goodbye", "exit", "quit"]):
        return "GOODBYE"
    elif "weather" in user_input:
        return "WEATHER"
    elif any(word in user_input for word in ["news", "whatsup"]):
        return "NEWS"
    elif any(word in user_input for word in ["joke", "funny"]):
        return "JOKE"
    elif any(word in user_input for word in ["help", "assist", "instructions"]):
        return "HELP"
    else:
        return "UNKNOWN"  # Default intent if no match is found

#Entity Extraction. 
def extract_location(user_input):
    # Simple location extraction using regular expressions (can be improved)
    match = re.search(r"(in|near|at|from)\s+(\w+)", user_input)  # Look for prepositions + location
    if match:
        return match.group(2)  # Return the captured location
    else:
        return None
    

def handle_intent(intent, location=None):
    if intent == "GREETING":
        responses = ["Hello, Sir!", "Greetings!", "Hi there!"]
        return random.choice(responses)
    elif intent == "GOODBYE":
        return "Goodbye, Sir! Until next time."
    elif intent == "WEATHER":
            if location:
                return get_weather(location)  # Call the get_weather function
            else:
                return "For what location would you like the weather?"
    elif intent == "JOKE":
        return get_joke() 
    elif intent == "NEWS":
      category = extract_news_category("general")
      return get_news(category) # Pass config to get_news
    elif intent == "HELP":
        return "I can help you with weather, jokes, and more. Just ask!"
    else:
        return "I'm not sure I understand.  Could you rephrase?"


def main():
    while True:
        user_input = input("You: ")
        intent = recognize_intent(user_input)
        if intent == "GOODBYE":
            print(handle_intent(intent))
            break

        location = extract_location(user_input) #extract the location
        response = handle_intent(intent, location) #send location to handle_intent()
        print("Jarvis:", response)


if __name__ == "__main__":
    main()