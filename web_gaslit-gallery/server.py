from flask import Flask, request
import base64
import os

app = Flask(__name__)

FLAG = os.environ.get('FLAG', 'sunctf26{41_c4nn0t_p4rs3_r34l1ty}')

@app.route('/')
def index():
    cookie = request.cookies.get('session')
    
    if cookie:
        try:
            decoded = base64.b64decode(cookie).decode('utf-8')
            role = decoded[::-1] 
            
            if role == 'admin':
                return f"<h1 style='color:green; font-family:monospace;'>Flag: {FLAG}</h1>"
        except Exception:
            pass

    try:
        with open('views/index.html', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: index.html not found in the views directory."

@app.route('/auth.js')
def serve_js():
    try:
        with open('views/auth.js', 'r') as file:
            return file.read(), 200, {'Content-Type': 'application/javascript'}
    except FileNotFoundError:
        return "Error: auth.js not found in the views directory.", 404

@app.route('/search')
def search():
    return "0 results found. Warning: Query logged by Sunway Intrusion Detection System."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)