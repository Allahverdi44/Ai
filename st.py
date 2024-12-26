from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Frontend ilə əlaqə üçün

# OpenAI API açarınızı burada qeyd edin
openai.api_key = "SIZIN_OPENAI_API_ACARINIZ"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Mesaj tapılmadı"}), 400

    try:
        # AI modelindən cavab alın
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sən bir süni intellekt yardımçısısan."},
                {"role": "user", "content": user_message}
            ]
        )

        ai_response = response['choices'][0]['message']['content']
        return jsonify({"reply": ai_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
