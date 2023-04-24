# Basic framework needed for flask to create a webpage
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
# run python3 app.py
# Page opens on http://localhost:5000/
