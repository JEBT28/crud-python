from logger import log
from controllers.personas import Personas
from models.persona import Persona
Personas = Personas()
def listarPersonas():
    try:
        result = Personas.getAll()
        if result is not None:
            for persona in result:
                print(persona)
        else:
            print("No hay personas registradas")
    except Exception as e:
        print(e)
    
    
def listarPersona():
    try:
        id = int(input("Ingrese el id de la persona a buscar: "))
        persona = Personas.getById(id)
        if persona is not None:
            print(persona)
        else:
            print("No se encontro la persona")
    except Exception as e:
        print(e)
    
def agregarPersona():
    try:
        nombre = input("Ingrese el nombre de la persona: ")
        apellido = input("Ingrese el apellido de la persona: ")
        email = input("Ingrese el email de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))

        persona = Persona(0, nombre, apellido, email, edad)
        isInserted = Personas.create(persona)
        if isInserted:
            print("Persona agregada correctamente")
        else:
            print("No se pudo agregar la persona")

    except Exception as e:
        print(e)

def actualizarPersona():
    
    try:
        id = int(input("Ingrese el id de la persona: "))
        result = Personas.getById(id)
        if result is None:
            print("No se encontro la persona")
            return
        persona = Persona(result[0],result[1],result[2],result[3],result[4])
        nombre = input(f"Nuevo nombre ({persona.nombre}): ") or persona.nombre
        apellido = input(f"Nuevo apellido ({persona.apellido}): ") or persona.apellido
        email = input(f"Nuevo email ({persona.email}): ") or persona.email
        edad = int(input(f"Nueva edad ({persona.edad}): ") or f"{persona.edad}")
        
        editado = Persona(0, nombre, apellido, email, edad)
        isEdited = Personas.updateById(id,editado)
        if isEdited:
            print("Persona agregada correctamente")
        else:
            print("No se pudo editar la persona")
    except Exception as e:
        print(e)
    
def eliminarPersona():
    try:
        id = int(input("Ingrese el id de la persona a eliminar: "))
        isDeleted = Personas.deleteById(id)
        if isDeleted:
            print("Persona eliminada correctamente")
        else:
            print("No se pudo eliminar la persona")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    
    while 1==1:
        print("1. Listar personas")
        print("2. Buscar persona por id")
        print("3. Crear persona")
        print("4. Actualizar persona")
        print("5. Eliminar persona")
    
        op = int(input("Ingrese una opcion: "))
        if op == 1:
            listarPersonas()
        elif op == 2:
            listarPersona()
        elif op == 3:
            agregarPersona()
        elif op == 4:
            actualizarPersona()
        elif op == 5:
            eliminarPersona()
        else:
            print("Opcion no valida")

        op = input('Press (c) to continue, (q) to quit: ')
        if op == 'q':
            exit()
