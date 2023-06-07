from datetime import datetime
from inicializacion import db
from werkzeug.security import generate_password_hash, check_password_hash
#conexion a base de datos
try:
     '''
     ------------------- Definicion de datos -------------------
     '''
     class aerolineas(db.Document):
          _id = db.IntField(required=True)
          nombre = db.StringField(required=True)
          pais = db.StringField(required=True)
          estado = db.StringField(required=True)
          

except IOError:
     print(IOError)
     