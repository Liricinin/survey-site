from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        genre = request.form.get("genre")
        return redirect(url_for("done", genre=genre))
    return render_template("survey.html")

@app.route("/done")
def done():
    genre = request.args.get("genre", "—")
    return render_template("done.html", genre=genre)

if __name__ == "__main__":
    app.run()
