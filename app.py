from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("app.html")

@app.route("/home")
def home():
    return "Welcome to the Home Page!"

if __name__ == "__main__":
    app.run()
