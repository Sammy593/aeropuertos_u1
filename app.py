#importacion de librerias
from os import abort
from inicializacion import app as app
import models as model
from flask import render_template, request, redirect, url_for, flash

#Buscar datos en la base de datos mongodb
import consultas as consultas

#aplicacion principal
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/aerolineas')
def aerolineas():
    return render_template('aerolineas/index.html')

@app.route('/aviones')
def aviones():
    return render_template('aviones/index.html')

@app.route('/boletos')
def boletos():
    return render_template('boletos/index.html')

@app.route('/vuelos')
def vuelos():
    return render_template('vuelos/index.html')

@app.route('/pasajeros')
def pasajeros():
    return render_template('pasajeros/index.html')

@app.route('/equipajes')
def equipajes():
    return render_template('equipajes/index.html')

# Ledesma

# Samuel

 #  Iniciando la aplicaciones
if __name__ == "__main__":
    app.secret_key = 'secret'
    app.run(debug=True)
