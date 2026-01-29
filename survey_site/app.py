from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return "СПАСИБО, ОПРОС ПРОЙДЕН"
    return """
    <form method="post">
      <p>Какой жанр нравится?</p>
      <input type="radio" name="genre" value="Древнерусская"> Древнерусская<br>
      <input type="radio" name="genre" value="Современная"> Современная<br>
      <input type="submit">
    </form>
    """

if name == "__main__":
    app.run()
