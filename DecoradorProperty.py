class Persona:
    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self._edad = edad
        pass
    
    @property#incluir property 
    def nombre(self): #getters
        return self.__nombre
    
    @nombre.setter#decorador 
    def nombre(self, new_nombre):# definir setters
         self.__nombre = new_nombre

    @nombre.deleter# deleter property 
    def nombre(self): 
        del self.__nombre
    
ale = Persona('Alexis',19)

nombre = ale.nombre#Llamar al getter
print(nombre)

ale.nombre = 'Pepe' #Llamar al setter

nombre = ale.nombre
print(nombre)

# del ale.nombre 
nombre = ale.nombre
print(nombre)
