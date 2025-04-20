from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "Dream big and dare to fail. – Norman Vaughan"
]

@app.route('/')
def index():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
