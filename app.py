from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to connect

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    # For now, dummy answer
    return jsonify({"answer": f"You asked: {question}. Student AI will answer soon!"})

@app.route("/flashcards", methods=["POST"])
def flashcards():
    topic = request.json.get("topic", "")
    cards = [
        {"front": "Photosynthesis", "back": "Process by which plants make food"},
        {"front": "Newton", "back": "Discovered gravity"}
    ]
    return jsonify({"topic": topic, "cards": cards})

@app.route("/quiz", methods=["POST"])
def quiz():
    topic = request.json.get("topic", "")
    questions = [
        {"q": "What is 2+2?", "options": ["3", "4", "5"], "answer": "4"},
        {"q": "Capital of India?", "options": ["Delhi", "Mumbai", "Kolkata"], "answer": "Delhi"}
    ]
    return jsonify({"topic": topic, "quiz": questions})

if __name__ == "__main__":
    app.run(debug=True)
