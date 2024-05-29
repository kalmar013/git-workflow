"""kom dla lint"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    """kom dla lint"""
    return '<h1>Hello WSB! Greetings from Flask!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
