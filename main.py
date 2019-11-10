from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def prva_stran():
    return render_template("prva-stran.html")

@app.route("/odgovor", methods=["post"])
def odgovor():
    ime = request.form.get("ime")
    sporocilo = request.form.get("sporocilo")
    return render_template("odgovor.html", ime=ime, sporocilo=sporocilo)

@app.route("/bogle")
def bogle():
    return render_template("bogle.html")

@app.route("/fakebook")
def fakebook():
    return render_template("fakebook.html")

@app.route("/frizer")
def frizer():
    return render_template("frizer.html")

if __name__ == '__main__':
    app.run()