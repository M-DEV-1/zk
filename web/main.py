from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from datetime import datetime
import pandas as pd 

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        chat_history = data.get('history', [])
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Build conversation context for Gemini
        conversation_context = []
        
        # Add chat history to context
        for msg in chat_history:
            if msg['role'] == 'user':
                conversation_context.append(f"User: {msg['content']}")
            else:
                conversation_context.append(f"Assistant: {msg['content']}")
        
        # Add current user message
        conversation_context.append(f"User: {user_message}")

        df = pd.read_csv('generated_dataset.csv', parse_dates=['timestamp'])
        userData = df.values.tolist()
        headers = list(df.columns)

        prompt = f"""
                                    Developer prompt: The admin will send you a message and i will send you some data along with it. you have to use this info to answer the admin prompt. Be crisp and to the point, answer in 2-3 lines. respond exactly only what the admin asks.
                                    Admin prompt: f{user_message}
                                    Data headers:  {headers}
                                    Data:""" + str(userData)
        
        # Create prompt with context
        if conversation_context:
            prompt = "\n".join(conversation_context[:-1]) + f"\n\n{prompt}\n\nAssistant:"
        else:
            prompt = f"User: {user_message}\n\nAssistant:"
        
        # Generate response from Gemini
        response = model.generate_content(prompt)
        bot_response = response.text
        
        return jsonify({
            'response': bot_response,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'error': 'Sorry, I encountered an error. Please try again.',
            'timestamp': datetime.now().isoformat()
        }), 500

if __name__ == '__main__':
    # Check if API key is set
    if not os.getenv('GEMINI_API_KEY'):
        print("Warning: GEMINI_API_KEY environment variable not set")
        print("Please set it with: export GEMINI_API_KEY='your_api_key_here'")
    
    app.run(debug=True, host='0.0.0.0', port=5000)