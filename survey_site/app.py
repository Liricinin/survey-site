from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        answer = request.form.get("genre")
        return f"Ты выбрал: {answer}"
    return render_template("survey.html")

if __name__ == "__main__":
    app.run()
