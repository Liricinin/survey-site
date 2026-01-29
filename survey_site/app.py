from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        genre = request.form.get("genre")

        # сохраняем ответ
        with open("answers.txt", "a", encoding="utf-8") as f:
            f.write(genre + "\n")

        return redirect("/done?genre=" + genre)

    return render_template("survey.html")


@app.route("/done")
def done():
    genre = request.args.get("genre")
    return render_template("done.html", genre=genre)


if name == "__main__":
    app.run()
