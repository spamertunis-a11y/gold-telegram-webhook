from flask import Flask, request
import requests
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    message = f"""
🟡 GOLD TRADE ALERT

Side: {data.get('side')}
Entry: {data.get('entry')}
SL: {data.get('sl')}
TP: {data.get('tp')}
Confidence: {data.get('confidence')}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": message
    })

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
