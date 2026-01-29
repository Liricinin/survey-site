from flask import Flask, render_template, request, redirect, make_response
import requests

app = Flask(__name__)


BOT_TOKEN = "8558607119:AAFOGlDrITQ3IFMcYiDVXeQnNp_Y_jgwz5c"
CHAT_ID = "5467355307"


def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)


@app.route("/", methods=["GET", "POST"])
def index():
 

    if request.method == "POST":
        answer = request.form.get("answer")

        if answer:
            send_to_telegram(f"📊 Новый ответ:\n{answer}")

        response = make_response(redirect("/done"))
        response.set_cookie("survey_done", "yes", max_age=60*60*24*365)
        return response

    return render_template("survey.html")


@app.route("/done")
def done():
    return render_template("done.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
