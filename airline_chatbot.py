import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

data = [
    {
        "intent": "greeting",
        "pattern": ["hi", "hello", "hey", "good morning", "good evening", "greetings", "hola"],
        "answer": "Hello! How can I assist you today with flight or cargo scheduling rules?"
    },
    {
        "intent": "farewell",
        "pattern": ["bye", "goodbye", "see you", "talk to you later", "farewell"],
        "answer": "Goodbye! Safe travels and happy scheduling 🛫"
    },
    {
        "intent": "cargo_weight",
        "pattern": ["What is the maximum cargo weight?", "What's the max cargo weight?", "How much weight can be carried?", "Cargo weight limit?"],
        "answer": "The maximum allowed cargo weight is 5000kg. Flights exceeding this are rejected."
    },
    {
        "intent": "restricted_hours",
        "pattern": ["Can a flight be scheduled during restricted hours in Delhi?", "When are flights restricted in Delhi?", "What are Delhi’s restricted flight hours?"],
        "answer": "Flights from Delhi between 2 AM and 4 AM are restricted unless it's an emergency."
    },
    {
        "intent": "weather_conditions",
        "pattern": ["What happens if the weather score is high?", "How does weather affect flight scheduling?", "Does the weather score delay flights?"],
        "answer": "If the weather risk score is above 6 and it's not an emergency, the flight will be delayed."
    },
    {
        "intent": "time_conflict",
        "pattern": ["What is considered a time conflict?", "What is a time conflict for a flight?", "How does the system check for time conflicts?"],
         "answer": "A time conflict occurs when two flights overlap in departure or arrival times and aren't emergency flights."
    },
    {
        "intent": "aircraft_availability",
        "pattern": ["How does the system check aircraft availability?", "How does the system schedule aircraft?", "Aircraft availability check?"],
        "answer": "The system checks if the aircraft is already scheduled for another flight during the requested time slot."
    }
]

# NLP Setup
all_questions = []
flat_answers = []

for item in data:
    for pattern in item["pattern"]:
        all_questions.append(pattern)
        flat_answers.append(item["answer"])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(all_questions)

def apply_rules(user_input):
    user_input = user_input.lower()
    for qa in data:
        for pattern in qa["pattern"]:
            if re.search(r"\b" + re.escape(pattern.lower()) + r"\b", user_input):
                return qa["answer"]
    return None

def get_response(user_input):
    response = apply_rules(user_input)
    if response:
        return response

    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, X)
    best_match_index = np.argmax(similarities)
    confidence = similarities[0][best_match_index]

    if confidence > 0.4:
        return flat_answers[best_match_index]
    else:
        return "Sorry, I couldn't understand that. Can you please rephrase?"

print("\n  Airline & Cargo Scheduler Chatbot ")
print("Ask me anything about flight rules! (type 'exit' or 'quit' to end the chat)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Bye! Feel free to come back anytime. ")
        break
    response = get_response(user_input)
    print(f"Chatbot: {response}\n")
