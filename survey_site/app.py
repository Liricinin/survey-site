from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # Если уже проходил опрос
    if request.cookies.get("survey_done") == "yes":
        return """
        <h1>Вы уже проходили опрос ✅</h1>
        <p>Спасибо за участие!</p>
        """

    if request.method == "POST":
        genre = request.form["genre"]

        response = make_response(f"""
        <h1>Спасибо за ответ! 📚</h1>
        <p><strong>Ваш выбор:</strong> {genre}</p>
        """)

        # Ставим cookie на 1 год
        response.set_cookie("survey_done", "yes", max_age=60*60*24*365)

        return response

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)