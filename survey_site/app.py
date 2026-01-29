from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Сайт работает ✅"

if name == "__main__":
    app.run()
