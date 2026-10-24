from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Audio Agency</h1><p>Investigating the sounds.</p>"
if __name__ == '__main__':
    app.run(debug=True, port=5000)
