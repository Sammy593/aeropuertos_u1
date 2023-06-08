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

""" ##############  Aerolineas ############### """   
@app.route('/aerolineas')
def aerolineas():
    lista_aerolineas = consultas.getAerolienas()
    return render_template('aerolineas/index.html', lista_aerolineas=lista_aerolineas)

@app.route('/form_add_aerolinea')
def form_add_aerolinea():
    return render_template('aerolineas/nuevo.html')     

@app.route('/add_aerolinea', methods=['POST'])
def add_aerolinea():
    if request.method == 'POST':
        nombre = request.form["nombre"]
        pais = request.form["pais"]
        estado = request.form["estado"]
        consultas.agregar_aerolinea(nombre, pais, estado)
    lista_aerolineas = consultas.getAerolienas()
    return render_template('aerolineas/index.html', lista_aerolineas=lista_aerolineas)

@app.route('/edit_aerolinea/<id>')
def edit_aerolinea(id):
    aerolinea = consultas.encontrar_aerolinea(id)
    return render_template('aerolineas/editar.html', aerolinea = aerolinea)

@app.route('/update_aerolinea/<id>', methods=['POST'])
def update_aerolinea(id):
    if request.method == 'POST':
        aerolinea_id = id
        nombre_aerolinea = request.form["nombre"]
        pais = request.form["pais"]
        estado = request.form["estado"]
        consultas.editar_aerolinea(aerolinea_id,nombre_aerolinea,pais,estado)
    return redirect(url_for("aerolineas"))

@app.route('/delete_aerolinea/<id>')
def delete_aerolinea(id):
    consultas.eliminar_aerolinea(id)  
    lista_aerolineas = consultas.getAerolienas()
    return render_template('aerolineas/index.html', lista_aerolineas=lista_aerolineas)

@app.route('/activar_aerolinea/<id>')
def activar_aerolinea(id):
    consultas.activa_aerolinea(id)  
    lista_aerolineas = consultas.getAerolienas()
    return render_template('aerolineas/index.html', lista_aerolineas=lista_aerolineas)


""" ##############  Boletos  ############### """
@app.route('/boletos')
def boletos():
    lista_boletos = consultas.getBoletos()
    return render_template('boletos/index.html', lista_boletos=lista_boletos)


"""           ##############  Aviones  ###############           """
@app.route('/aviones')
def aviones():
    lista_aviones = consultas.getAviones()
    return render_template('aviones/index.html', lista_aviones=lista_aviones)

@app.route('/form_add_avion')
def form_add_avion():
    lista_aerolineas = consultas.getAerolienasActivas()
    return render_template('aviones/nuevo.html', lista_aerolineas=lista_aerolineas)     

@app.route('/add_avion', methods=['POST'])
def add_avion():
    if request.method == 'POST':
        idAerolinea = request.form["idAerolinea"]
        modelo = request.form["modelo"]
        capacidad_de_pasajeros = request.form["capacidad_de_pasajeros"]
        estado = request.form["estado"]
        consultas.agregar_avion(idAerolinea,modelo,capacidad_de_pasajeros,estado)
    lista_aviones = consultas.getAviones()
    return render_template('aviones/index.html', lista_aviones=lista_aviones)

@app.route('/edit_avion/<id>')
def edit_avion(id):
    avion = consultas.encontrar_avion(id)
    lista_aerolineas = consultas.getAerolienasActivas()
    return render_template('aviones/editar.html', avion = avion, lista_aerolineas=lista_aerolineas)

@app.route('/update_avion/<id>', methods=['POST'])
def update_avion(id):
    if request.method == 'POST':
        avionId = id
        idAerolinea = request.form["idAerolinea"]
        modelo = request.form["modelo"]
        capacidad_de_pasajeros = request.form["capacidad_de_pasajeros"]
        estado = request.form["estado"]
        consultas.editar_avion(avionId,idAerolinea,modelo,capacidad_de_pasajeros,estado)
    return redirect(url_for("aviones"))

@app.route('/delete_avion/<id>')
def delete_avion(id):
    consultas.eliminar_avion(id)  
    lista_aviones = consultas.getAviones()
    return render_template('aviones/index.html', lista_aviones=lista_aviones)

@app.route('/activar_avion/<id>')
def activar_avion(id):
    consultas.activa_avion(id)  
    lista_aviones = consultas.getAviones()
    return render_template('aviones/index.html', lista_aviones=lista_aviones)

""" ##############  Vuelos  ############### """

@app.route('/vuelos')
def vuelos():
    lista_vuelos = consultas.getVuelos()
    return render_template('vuelos/index.html', lista_vuelos=lista_vuelos)

@app.route('/btn_vender_vuelo/<id>')
def btn_vender_vuelo(id):
    vuelo = consultas.getVuelo(id)
    pasajeros = consultas.getPasajeros()
    return render_template('vuelos/boleto.html', pasajeros=pasajeros, vuelo=vuelo)

@app.route('/vender_boleto_vuelo', methods=['POST'])
def vender_boleto_vuelo():
    if request.method == 'POST':
        id_vuelo = request.form["id_vuelo"]
        n_asiento = request.form["n_asiento"]
        clase = request.form["clase"]
        id_pasajero = request.form["id_pasajero"]
        consultas.vender_boleto(id_vuelo,n_asiento,clase,id_pasajero)
    return redirect(url_for("vuelos"))

@app.route('/form_add_vuelo')
def form_add_vuelo():
    lista_aerolineas = consultas.getAerolienas()
    lista_aviones = consultas.getAviones()
    return render_template('vuelos/nuevo.html', lista_aerolineas=lista_aerolineas, lista_aviones=lista_aviones)

@app.route('/add_vuelo', methods=['POST'])
def add_vuelo():
    if request.method == 'POST':
        idAvion = request.form["idAvion"]
        precio = request.form["precio"]
        origen = request.form["origen"]
        destino = request.form["destino"]
        fecha_salida = request.form["fecha_salida"]
        estado = request.form["estado"]
        consultas.agregar_vuelo(idAvion,precio, origen, destino, fecha_salida, estado)
    lista_vuelos = consultas.getVuelos()
    return render_template('vuelos/index.html', lista_vuelos=lista_vuelos)

@app.route('/edit_vuelo/<id>')
def edit_vuelo(id):
    vuelo = consultas.encontrar_vuelo(id)
    lista_aerolineas = consultas.getAerolienas()
    lista_aviones = consultas.getAviones()
    return render_template('vuelos/editar.html', vuelo = vuelo, lista_aerolineas=lista_aerolineas, lista_aviones=lista_aviones)

@app.route('/update_vuelo/<id>', methods=['POST'])
def update_vuelo(id):
    if request.method == 'POST':
        vuelo_id = id
        idAvion = request.form["idAvion"]
        precio = request.form["precio"]
        origen = request.form["origen"]
        destino = request.form["destino"]
        fecha_salida = request.form["fecha_salida"]
        estado = request.form["estado"]
        consultas.editar_vuelo(vuelo_id,precio,idAvion,origen,destino,fecha_salida,estado)
    return redirect(url_for("vuelos"))

@app.route('/delete_vuelo/<id>')
def delete_vuelo(id):
    consultas.eliminar_vuelo(id)  
    lista_vuelos = consultas.getVuelos()
    return render_template('vuelos/index.html', lista_vuelos=lista_vuelos)


# Jhostyn
""" ------------------------------ PASAJEROS ------------------------------"""
@app.route('/pasajeros')
def pasajeros():
    lista_pasajeros = consultas.getPasajeros()
    return render_template('pasajeros/index.html', lista_pasajeros=lista_pasajeros)

@app.route('/form_add_pasajero')
def form_add_pasajero():
    return render_template('pasajeros/nuevo.html')     

@app.route('/add_pasajero', methods=['POST'])
def add_pasajero():
    if request.method == 'POST':
        ci = request.form["ci"]
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        edad = request.form["edad"]
        consultas.agregar_pasajero(ci,nombre, apellido, edad)
    lista_pasajeros = consultas.getPasajeros()
    return render_template('pasajeros/index.html', lista_pasajeros=lista_pasajeros)

@app.route('/edit_pasajero/<id>')
def edit_pasajero(id):
    pasajero = consultas.encontrar_pasajero(id)
    return render_template('pasajeros/editar.html', pasajero = pasajero)

@app.route('/update_pasajero/<id>', methods=['POST'])
def update_pasajero(id):
    if request.method == 'POST':
        pasajero_id = id
        ci = request.form["ci"]
        nombre_pasajero = request.form["nombre"]
        apellido = request.form["apellido"]
        edad = request.form["edad"]
        consultas.editar_pasajero(pasajero_id,ci,nombre_pasajero, apellido, edad)
    return redirect(url_for("pasajeros"))


@app.route('/delete_pasajero/<id>')
def delete_pasajero(id):
    consultas.eliminar_pasajero(id)  
    lista_pasajeros = consultas.getPasajeros();
    return render_template('pasajeros/index.html', lista_pasajeros=lista_pasajeros)


""" ------------------------------ EQUIPAJES  ------------------------------"""
@app.route('/equipajes')
def equipajes():
    lista_equipajes = consultas.getEquipajes()
    pasajeros = consultas.getPasajeros()
    return render_template('equipajes/index.html',lista_equipajes=lista_equipajes,pasajeros = pasajeros)


@app.route('/form_add_equipaje')
def form_add_equipaje():
    pasajeros = consultas.getPasajeros()
    return render_template('equipajes/nuevo.html', pasajeros = pasajeros)     

@app.route('/add_equipaje', methods=['POST'])
def add_equipajes():
    if request.method == 'POST':
        descripcion = request.form["descripcion"]
        peso = request.form["peso"]
        idPasajero = request.form["idPasajero"]
        estado = request.form["estado"]
        consultas.agregar_equipaje(descripcion, peso, idPasajero, estado)
    lista_equipajes = consultas.getEquipajes()
    pasajeros = consultas.getPasajeros()
    return render_template('equipajes/index.html', lista_equipajes=lista_equipajes, pasajeros = pasajeros)


@app.route('/edit_equipaje/<id>')
def edit_equipaje(id):
    equipaje = consultas.encontrar_equipaje(id)
    pasajeros = consultas.getPasajeros()
    return render_template('equipajes/editar.html', equipaje = equipaje, pasajeros = pasajeros)

@app.route('/update_equipaje/<id>', methods=['POST'])
def update_equipaje(id):
    if request.method == 'POST':
        descripcion = request.form["descripcion"]
        peso = request.form["peso"]
        idPasajero = request.form["idPasajero"]
        estado = request.form["estado"]
        consultas.agregar_equipaje(descripcion, peso, idPasajero, estado)
    return redirect(url_for("equipajes"))


@app.route('/delete_equipaje/<id>')
def delete_equipaje(id):
    consultas.eliminar_equipaje(id)  
    lista_equipajes = consultas.getEquipajes()
    pasajeros = consultas.getPasajeros()
    return render_template('equipajes/index.html',lista_equipajes=lista_equipajes,pasajeros = pasajeros)


# Ledesma

# Samuel

 #  Iniciando la aplicaciones
if __name__ == "__main__":
    app.secret_key = 'secret'
    app.run(debug=True)
