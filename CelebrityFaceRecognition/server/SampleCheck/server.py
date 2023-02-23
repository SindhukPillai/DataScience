from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')

def hello():
    return "Hi Sindhu"

if __name__ == "__main__":
    print("Starting Python Flask Server For sample testing")
    app.run(port=5000)