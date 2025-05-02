from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
    
    if request.method == 'GET':
        #Whatsapp webhook verification
        verify_token = 'custom-123'
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode and token == verify_token:
            return challenge, 200
        else:
            return "Verification failed", 403
        
    elif request.method == 'POST':
        # This is where incoming messages are handled
        data = request.get_json()
        print("[Incoming Webhook Data]", data)

        return jsonify({"Status": "received"}), 200
    
if __name__ == '__main__':
    app.run(port=5000)
    
