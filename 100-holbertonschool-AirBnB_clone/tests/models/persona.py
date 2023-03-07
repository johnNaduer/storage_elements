class Persona:
    def __init__(self,segundo_apellido):
        self.nombre = "john"
        self.segundo_apellido = segundo_apellido
    def __str__(self):
        return "[{}] {}".format(self.__class__.__name__, self.__dict__)
    
nombre1 = Persona("yaros")
nombre1.primer_nombre = "naduer"
nombre1.apellido = "espino"
nombre1.edad = 30
print(nombre1)
