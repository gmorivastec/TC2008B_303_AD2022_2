from flask import Flask
import sys
import random

app = Flask(__name__)

@app.route("/")
def principal():
    puntos = []

    # loop para generar carritos internos
    for i in range(10):
        puntos.append({"id": i, "x": i, "y": i, "z": i});
        
        # COMO HACER PRINT
        print('así se imprime' , file=sys.stdout)

        # COMO SACAR VALORES RANDOM
        random.uniform(0, 10)

    return {"carros": puntos}