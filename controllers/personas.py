from connection import connection 
from dotenv import dotenv_values

from models.persona import Persona

config = dotenv_values(".env")

class Personas:
    _conn = None
    
    def __init__(self) -> None:
        self._conn = connection(config['HOST'], config['PORT'], config['DB'], config['USER'], config['PASS'])
        
    def getAll(self):
        try:
            cursor = self._conn.getCursor()
            cursor.execute("SELECT * FROM personas")
            result = cursor.fetchall()

            return result
        except Exception as e:
            print(e)
            return None

    def getById(self, id):
        try:
            cursor = self._conn.getCursor()
            cursor.execute("SELECT * FROM personas WHERE idPersona = %s", (id,))
            result = cursor.fetchone()
            self._conn.close()
            return result
        except Exception as e:
            print(e)
            return None
    
    def create(self, persona: Persona):
        try:
            cursor = self._conn.getCursor()
            cursor.execute("INSERT INTO personas (nombre, apellido, email, edad) VALUES (%s, %s, %s, %s)", (persona.nombre , persona.apellido, persona.email, persona.edad))
            self._conn.commit()
            self._conn.close()
            return True
        except Exception as e:
            print (e)
            
    def updateById(self, id, persona: Persona):
        try:
            cursor = self._conn.getCursor()
            cursor.execute("UPDATE personas SET nombre = %s, apellido = %s, email = %s, edad = %s WHERE idPersona = %s", (persona.nombre, persona.apellido, persona.email, persona.edad,id))
            self._conn.commit()
            self._conn.close()
            return True
        except Exception as e:
            print (e)
            
    def deleteById(self, id):
        try:
            cursor = self._conn.getCursor()
            cursor.execute("DELETE FROM personas WHERE idPersona = %s", (id,))
            self._conn.commit()
            self._conn.close()
            return True
        except Exception as e:
            print (e)