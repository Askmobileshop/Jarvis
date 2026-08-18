from flask import Flask,request

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Ask Mobile Shop!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == "ask.143":
            return challenge, 200
        else:
            return "Invalid verification token", 403
    elif request.method == "POST":
        return "OK", 200
