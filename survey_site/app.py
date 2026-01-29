from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        genre = request.form.get("genre")
        return redirect(f"/done?genre={genre}")
    return render_template("survey.html")

@app.route("/done")
def done():
    choice = request.args.get("genre")
    return render_template("done.html", choice=choice)
