from flask import Flask

app = Flask(__name__)

@app.route("/hola/<nombre>")
def hola(nombre):
    return f"Hola, {nombre}"

if __name__ == "__main__":
    app.run(debug=True)