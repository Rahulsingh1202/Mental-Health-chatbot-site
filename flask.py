from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Predefined responses for mental health-related issues
responses = {
    "anxiety": [
        "It's okay to feel anxious sometimes. Try taking deep breaths and focus on things you can control.",
        "Anxiety can be overwhelming, but practicing mindfulness and talking to a therapist can help."
    ],
    "depression": [
        "I'm sorry you're feeling down. Talking to a close friend or therapist can make a difference.",
        "Depression is tough, but remember, you don't have to face it alone."
    ],
    "stress": [
        "Stress can be challenging. Try relaxation exercises or take small breaks to recharge.",
        "Managing stress can be easier when you break tasks into smaller steps."
    ],
    "default": [
        "I'm here for you. Can you tell me more about what you're feeling?",
        "Remember, reaching out to others can be a big step toward feeling better."
    ]
}

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for chatbot conversation
@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get("message").lower()
    
    # Find a relevant response based on keywords
    if "anxiety" in user_message:
        response = random.choice(responses["anxiety"])
    elif "depression" in user_message:
        response = random.choice(responses["depression"])
    elif "stress" in user_message:
        response = random.choice(responses["stress"])
    else:
        response = random.choice(responses["default"])

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
