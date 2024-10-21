import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Initialize Groq client with your API key
client = Groq(api_key="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")  # Replace with your actual API key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    try:
        # Call Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            model="mixtral-8x7b-32768",  # You can change this to a different model if needed
            max_tokens=1000
        )
        
        ai_response = chat_completion.choices[0].message.content
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
