from operator import mod
import models as model



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


"""    ##############  """