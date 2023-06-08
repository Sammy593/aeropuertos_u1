import models as modelo

aerolinea = modelo.aerolineas(
    _id = "1",
    nombre = "Tame",
    pais = "EEUU",
    estado = "Activo"
)

boleto = modelo.boletos(
    _id = "1",
    id_vuelo = "1",
    fecha = "2014-11-24",
    n_asiento = "12",
    clase = "Primera clase",
    id_pasajero = "1"
)

pasajero = modelo.pasajeros(
    _id = "1",
    ci = "123456",
    nombre = "Pasajero 1",
    apellido = "A Pasajero",
    edad = 30
)

equipaje = modelo.equipajes(
    _id = "1",
    descripcion = "Descripcion",
    peso = 12.45,
    idPasajero = "1",
    estado = "Activo"
)

vuelo = modelo.vuelos(
    _id = "1",
    idAvion = "1",
    precio = 25678.135,
    origen = "ALE"     ,
    destino = "Brasil",
    fecha_salida = "2014-11-24",
    estado = "Activo"
)

avion = modelo.aviones(
    _id = "1",
    idAerolinea = "1",
    modelo = "N123",
    capacidad_de_pasajeros = 100,
    estado = "Activo"
)


aerolinea.save()
boleto.save()
pasajero.save()
equipaje.save()
vuelo.save()
avion.save()