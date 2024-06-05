from flask import Flask

app = Flask(__name__)

@app.route("/hola/<nombre>")
def hola(nombre):
    return f"Hola, {nombre}"

@app.route("/saludo/<saludo>/<nombre>")
def saludo_personalizado(saludo, nombre):
    return f"{saludo}, {nombre}"

if __name__ == "__main__":
    app.run(debug=True)