from flask import Flask

app = Flask (__name__)

@app.route("/hola")
def hola():
    return "hola mami"

@app.route("/adios")
def chau():
    return("chau")

app.run()