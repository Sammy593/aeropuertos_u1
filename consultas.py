from operator import mod
import models as model
##from bson.objectid import ObjectId
import uuid


"""    CRUD aerolineas  """
def getAerolienas():
    try:
        aerolineasList = []
        for i in model.aerolineas.objects():
            aerolinea = {
                '_id': i["_id"],
                'nombre': i["nombre"],
                'pais': i["pais"],
                'estado': i["estado"]
            }
            aerolineasList.append(aerolinea)
        return aerolineasList
    except IOError:
        return IOError

def getAerolienasActivas():
    try:
        aerolineasList = []
        for i in model.aerolineas.objects(estado = "Activo"):
            aerolinea = {
                '_id': i["_id"],
                'nombre': i["nombre"],
                'pais': i["pais"],
                'estado': i["estado"]
            }
            aerolineasList.append(aerolinea)
        return aerolineasList
    except IOError:
        return IOError
    
def agregar_aerolinea(pnombre, ppais, pestado):
     try:
          idA = str(uuid.uuid4())
          aerolinea = model.aerolineas(
                _id= idA,
                nombre= pnombre,
                pais = ppais,
                estado = pestado
          )
          aerolinea.save() 
     except IOError:
       return IOError 

def encontrar_aerolinea(id):
    aerolinea = model.aerolineas.objects.get(_id=id)
    return aerolinea
        
def editar_aerolinea(paerolinea_id, pnombre_aerolinea,ppais,pestado):
     aerolinea = encontrar_aerolinea(paerolinea_id)
     
     aerolinea.update(
          nombre= pnombre_aerolinea,
          pais = ppais,
          estado = pestado
     )
     return False

def eliminar_aerolinea(id): 
     try:
        aerolinea = model.aerolineas.objects.get(_id=id)
        aerolinea.estado = "Inactivo"
        aerolinea.save()
        return True
     except IOError:
        print(IOError)

def activa_aerolinea(id): 
     try:
        aerolinea = model.aerolineas.objects.get(_id=id)
        aerolinea.estado = "Activo"
        aerolinea.save()
        return True
     except IOError:
        print(IOError)


"""    CRUD boletos  """
def getBoletos():
    try:
        boletosList = []
        for i in model.boletos.objects():
            boleto = {
                '_id': i["_id"],
                'vuelo': i["id_vuelo"],
                'fecha': i["fecha"],
                'n_asiento': i["n_asiento"],
                'clase': i["clase"],
                'id_pasajero': i["id_pasajero"]
            }
            boletosList.append(boleto)
        return boletosList
    except IOError:
        return IOError

"""    CRUD vuelos  """
def getVuelo(id):
    try:
        vuelo = model.vuelos.objects.get(_id = id)
        return vuelo
    except IOError:
        return IOError 
def getVuelos():
    try:
        vuelosList = []
        for i in model.vuelos.objects():
            vuelo = {
                '_id': i["_id"],
                'idAvion': i["idAvion"],           
                'precio': i["precio"],
                'origen': i["origen"],
                'destino': i["destino"],
                'fecha_salida': i["fecha_salida"],
                'estado': i["estado"]
            }
            vuelosList.append(vuelo)
        return vuelosList
    except IOError:
        return IOError

def vender_boleto(pid_vuelo,pn_asiento,pclase,pid_pasajero):
    try:
        idA = str(uuid.uuid4())
        boleto = model.boletos(
          _id = idA,
          id_vuelo = pid_vuelo,
          n_asiento = pn_asiento,
          clase = pclase,
          id_pasajero = pid_pasajero,
        )
        boleto.save() 
    except IOError:
        return IOError
    
def agregar_vuelo(pavion, pprecio, porigen, pdestino, pfecha_salida, pestado):
    try:
        idV = str(uuid.uuid4())
        vuelo = model.vuelos(
            _id= idV,
            idAvion=pavion,
            precio=pprecio,
            origen=porigen,
            destino=pdestino,
            fecha_salida=pfecha_salida,
            estado=pestado
        )
        vuelo.save()
    except IOError:
        return IOError
        
def encontrar_vuelo(id):
    vuelo = model.vuelos.objects.get(_id=id)
    return vuelo

def editar_vuelo(pvuelo_id, pprecio, pavion, porigen, pdestino, pfecha_salida, pestado):
    vuelo = encontrar_vuelo(pvuelo_id)
    vuelo.update(
        precio=pprecio,
        idAvion=pavion,
        origen=porigen,
        destino=pdestino,
        fecha_salida=pfecha_salida,
        estado=pestado
    )
    return False

def eliminar_vuelo(id):
    try:
        vuelo = model.vuelos.objects.get(_id=id)
        vuelo.estado = "Inactivo"
        vuelo.save()
        return True
    except IOError:
        print(IOError)

"""   CRUD Aviones """
def encontrar_avion(id):
    try:
        avion = model.aviones.objects.get(_id=id)
        return avion
    except IOError:
        print(IOError)

def getAviones():
    try:
        avionesList = []
        for i in model.aviones.objects():
            aerolinea = model.aerolineas.objects.get(_id = i["idAerolinea"])
            if(aerolinea['estado'] != "Activo"):
                aerolinea = "Sin asignar"
            else:
                aerolinea = aerolinea['nombre']
            
            avion = {
                '_id': i["_id"],
                'aerolinea': aerolinea,
                'modelo': i["modelo"],
                'capacidad_de_pasajeros': i["capacidad_de_pasajeros"],
                'estado': i["estado"]
            }
            avionesList.append(avion)
        return avionesList
    except IOError:
        return IOError


def agregar_avion(idAerolinea,modelo,capacidad_de_pasajeros,estado):
    try:
        idA = str(uuid.uuid4())
        avion = model.aviones(
          _id = idA,
         idAerolinea = idAerolinea,
         modelo = modelo,
         capacidad_de_pasajeros = capacidad_de_pasajeros,
         estado = estado
        )
        avion.save() 
    except IOError:
        return IOError

def editar_avion(avionId,idAerolinea,modelo,capacidad_de_pasajeros,estado):
     avion = encontrar_avion(avionId)
     
     avion.update(
         idAerolinea = idAerolinea,
         modelo = modelo,
         capacidad_de_pasajeros = capacidad_de_pasajeros,
         estado = estado
     )
     return False


def eliminar_avion(id): 
     try:
        avion = model.aviones.objects.get(_id=id)
        avion.estado = "Inactivo"
        avion.save()
        return True
     except IOError:
        print(IOError)

def activa_avion(id): 
     try:
        avion = model.aviones.objects.get(_id=id)
        avion.estado = "Activo"
        avion.save()
        return True
     except IOError:
        print(IOError)



""" ##############  CRUD Pasajeros  ##############"""
def getPasajeros():
    try:
        pasajerosList = []
        for i in model.pasajeros.objects():
            pasajero = {
                '_id': i["_id"],
                'ci': i["ci"],
                'nombre': i["nombre"],
                'apellido': i["apellido"],
                'edad': i["edad"]
            }
            pasajerosList.append(pasajero)
        return pasajerosList
    except IOError:
        return IOError

# ****************** Agregar Pasajero *******************
def agregar_pasajero(pci, pnombre, papellido, pedad):
     try:
          idP = str(uuid.uuid4())
          pasajero = model.pasajeros(
                _id= idP,
                ci = pci,
                nombre = pnombre,
                apellido = papellido,
                edad = pedad
          )
          pasajero.save() 
     except IOError:
       return IOError 

def encontrar_pasajero(id):
    pasajero = model.pasajeros.objects.get(_id=id)
    return pasajero
        
def editar_pasajero(ppasajero_id, pci,pnombre_pasajero,papellido,pedad):
     pasajero = encontrar_pasajero(ppasajero_id)
     
     pasajero.update(
          ci = pci,
          nombre= pnombre_pasajero,
          apellido = papellido,
          edad = pedad
     )
     return False

"""def eliminar_pasajero(id): 
     try:
          pasajero = model.pasajeros.objects.get(_id=ObjectId(id))
          pasajero.delete()
          return True
     except:
          return False
"""
def eliminar_pasajero(id): 
     try:
        pasajero = model.pasajeros.objects.get(_id=id)
        pasajero.delete()
        return True
     except IOError:
        print(IOError)
""" ##############  Fin Pasajeros ############## """

""" ##############  CRUD Equipajes  ############## """
def getEquipajes():
    try:
        equipajesList = []
        for i in model.equipajes.objects():
            equipaje = {
                '_id': i["_id"],
                'descripcion': i["descripcion"],
                'peso': i["peso"],
                'idPasajero': i["idPasajero"],
                'estado': i["estado"]
            }
            equipajesList.append(equipaje)
        return equipajesList
    except IOError:
        return IOError

    
def agregar_equipaje(pdescripcion, ppeso, pidPasajero, pestado):
    try:
        idE = str(uuid.uuid4())
        equipaje = model.equipajes(
            _id=idE,
            descripcion=pdescripcion,
            peso=ppeso,
            idPasajero=pidPasajero,  
            estado=pestado
        )
        equipaje.save() 
    except IOError:
        return IOError




def encontrar_equipaje(id):
    equipaje = model.equipajes.objects.get(_id=id)
    return equipaje
        
def editar_equipaje(pequipaje_id, pdescripcion,ppeso,pidPasajero,pestado):
     equipaje = encontrar_equipaje(pequipaje_id)
     
     equipaje.update(
          descripcion= pdescripcion,
          peso = ppeso,
          pidPasajero = pidPasajero, 
          estado = pestado
     )
     return False


def eliminar_equipaje(id): 
     try:
        equipaje = model.equipajes.objects.get(_id=id)
        equipaje.delete()
        return True
     except IOError:
        print(IOError)
""" ##############  Fin Equipaje############## """

