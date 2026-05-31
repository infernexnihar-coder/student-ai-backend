from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load a free Hugging Face model
qa_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")

    # Simple context for demo
    context = "Student AI is a learning assistant that helps answer questions for students."

    try:
        result = qa_model(question=question, context=context)
        answer = result["answer"]
    except Exception as e:
        answer = f"Error: {str(e)}"

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
