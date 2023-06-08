from datetime import datetime
from inicializacion import db
from werkzeug.security import generate_password_hash, check_password_hash
#conexion a base de datos

try:
     '''
     ------------------- Definicion de datos -------------------
     '''
     class aerolineas(db.Document):
          _id = db.StringField(primary_key = True)
          nombre = db.StringField(required=True)
          pais = db.StringField(required=True)
          estado = db.StringField(required=True)

     class boletos(db.Document):
          _id = db.StringField(primary_key = True)
          id_vuelo = db.StringField(required=True)
          fecha = db.DateTimeField(default=datetime.utcnow)
          n_asiento = db.StringField(required=True)
          clase = db.StringField(required=True)
          id_pasajero = db.StringField(required=True)
          
     class pasajeros(db.Document):
          _id = db.StringField(primary_key = True)
          ci = db.StringField(required=True)
          nombre = db.StringField(required=True)
          apellido = db.StringField(required=True)
          edad = db.IntField(required=True)

     class equipajes(db.Document):
          _id = db.StringField(primary_key = True)
          descripcion = db.StringField(required=True)
          peso = db.FloatField(required=True)
          idPasajero = db.StringField(required=True)
          estado = db.StringField(required=True)
     
     class vuelos(db.Document):
          _id = db.StringField(primary_key = True)
          idAvion = db.StringField(required=True)
          precio = db.FloatField(required=True)
          origen = db.StringField(required=True)          
          destino = db.StringField(required=True)
          fecha_salida = db.DateTimeField(default=datetime.utcnow)
          estado = db.StringField(required=True)

     class aviones(db.Document):
          _id = db.StringField(primary_key = True)
          idAerolinea = db.StringField(required=True)
          modelo = db.StringField(required=True)
          capacidad_de_pasajeros = db.IntField(required=True)
          estado = db.StringField(required=True)

except IOError:
     print(IOError)
     