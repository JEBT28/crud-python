class Persona:
    _idPersona = 0
    _nombre = ''
    _apellido = ''
    _email = ''
    _edad = 0
    
    
    def __init__(self, id, nombre,apellido, email, edad):
        self._idPersona = id
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._edad = edad
        
   # Getter and setters with @property decorator
    @property
    def idPersona(self):
        return self._idPersona
    
    @idPersona.setter
    def idPersona(self, id):
        self._idPersona = id
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
        
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
        
    def __str__(self):
        return "Id: " + str(self._id) + " Nombre: " + self._nombre + " Apellido: " + self._apellido + " Email: " + self._email + " Edad: " + str(self._edad)