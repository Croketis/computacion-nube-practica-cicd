# Practica CI/CD - Computacion en la Nube
# App Flask sencilla para probar despliegue en Azure

from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Hola! La app esta funcionando. Probar /api/status"


@app.route("/api/status")
def status():
    respuesta = {
        "status": "ok",
        "mensaje": "App desplegada correctamente en Azure",
        "fecha": str(datetime.datetime.now())
    }
    return jsonify(respuesta)


if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=puerto, debug=True)
