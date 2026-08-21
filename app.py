from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to A.S.K Mobile Shop"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if mode and token:
            if mode == 'subscribe' and token == 'Ask_143':
                return challenge, 200
            else:
                return 'Forbidden', 403
        return 'Error', 400
    
    elif request.method == 'POST':
        data = request.json
        print(data) 
        return 'ok',200
