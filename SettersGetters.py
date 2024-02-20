class Persona:
    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self.__edad = edad
        pass
    def get_nombre(self):#definir getters
        return self.__nombre
    
    def set_nombre(self, new_nombre):# definir setters
         self.__nombre = new_nombre

ale = Persona('Alexis',19)

nombre = ale.get_nombre()
print(nombre)

ale.set_nombre('Juan')

nombre = ale.get_nombre()
print(nombre)