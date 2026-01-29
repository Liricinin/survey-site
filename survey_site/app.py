from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        genre = request.form.get("genre")
        print("Ответ:", genre)  # для логов
        return redirect(url_for("done"))
    return render_template("survey.html")

@app.route("/done")
def done():
    return render_template("done.html")

if __name__ == "__main__":
    app.run(debug=True)