import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

WHATSAPP_TOKEN = "AIzaSyCvV9HImlX_1hpiXjSEy6Qui20JiRZAeNU"
PHONE_NUMBER_ID = "1253206694543330"
VERIFY_TOKEN = "Ask.143"

@app.route('/')
def home():
    return "Welcome to ASK Mobile Shop"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if mode and token:
            if mode == 'subscribe' and token == VERIFY_TOKEN:
                return challenge, 200
            else:
                return 'Forbidden', 403
        return 'Error', 400
    
    elif request.method == 'POST':
        data = request.json
        print(data)
        
        try:
            entry = data.get('entry', [])[0]
            changes = entry.get('changes', [])[0]
            value = changes.get('value', {})
            messages = value.get('messages', [])
            
            if messages:
                message = messages[0]
                from_phone = message.get('from')
                
                reply_text = "नमस्ते! ASK Mobile Shop में आपका स्वागत है। आपका संदेश मिल गया है, हम जल्द ही आपसे संपर्क करेंगे।"
                
                headers = {
                    "Authorization": f"Bearer {WHATSAPP_TOKEN}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "messaging_product": "whatsapp",
                    "to": from_phone,
                    "type": "text",
                    "text": {"body": reply_text}
                }
                
                url = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"
                requests.post(url, json=payload, headers=headers)
                
        except Exception as e:
            print(f"Error handling message: {e}")
            
        return 'ok', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
