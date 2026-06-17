from flask import Flask, render_template
from sqlalchemy import create_engine, text
from config import DATABASE_URL

app = Flask(__name__)

engine = create_engine(DATABASE_URL)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register():
    return "<h2>Student Registration Page</h2>"

@app.route("/dashboard")
def dashboard():
    return "<h2>Dashboard Page</h2>"

if __name__ == "__main__":
    app.run(debug=True)