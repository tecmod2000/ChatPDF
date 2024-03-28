class Persona:
  def __init__(self1, nombre, edad):
    self1.nombre = nombre
    self1.edad = edad

  def saludar(self1):
    print("Hola, mi nombre es %s y tengo %d años." % (self1.nombre, self1.edad))

# Crear un objeto de la clase Persona
persona = Persona("Juan", 30)

# Llamar al método saludar del objeto
persona.saludar()