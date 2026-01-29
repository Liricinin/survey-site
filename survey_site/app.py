@app.route("/done")
def done():
    choice = request.args.get("genre")
    return render_template("done.html", choice=choice)
