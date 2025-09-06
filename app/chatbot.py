
from flask import Blueprint, request, jsonify
import google.generativeai as genai
import os

chatbot_blueprint = Blueprint('chatbot', __name__)

# Configure Gemini with your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini Pro model
model = genai.GenerativeModel("gemini-2.0-flash")

@chatbot_blueprint.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "Message is required"}), 400

    try:
        # Generate AI response
        response = model.generate_content(
            f"""
            You are a supportive mental health assistant for college students.
            Keep replies short, empathetic, stigma-free, and encouraging.
            If the user shows signs of distress, gently recommend seeking
            professional counseling.

            User: {message}
            Assistant:
            """
        )
        reply = response.text.strip()
        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
