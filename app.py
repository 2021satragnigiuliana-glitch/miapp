# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

def dar_consejo (temperatura, llueve):
    if temperatura < 10:
        consejo = "Hace frío, usa abrigo."
    elif temperatura <= 24:
        consejo = "La temperatura es agradable, usá ropa cómoda."
    else:
        consejo = "Hace calor, usa ropa ligera."

    if llueve == "s":
        consejo += " No olvides llevar paraguas."

    return consejo

@app.route("/", methods=["GET", "POST"])
def inicio():
    consejo = ""

    if request.method == "POST":
        temperatura = int(request.form["temperatura"])
        llueve = request.form["llueve"]

        consejo = dar_consejo(temperatura, llueve)

    return render_template("index.html", consejo=consejo)

if __name__ == "__main__":
    app.run(debug=True)
