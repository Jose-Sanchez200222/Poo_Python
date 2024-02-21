from abc import ABC, abstractclassmethod#esto es un decorador 'abstractclassmethod'

class Persona(ABC):
    @abstractclassmethod#Declarar una clase abstracta
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod#obliga que lo implementa, evita errores,Fomenta el polimorfismo
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f'Hola me llamo {self.nombre} y tengo {self.edad} años')
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        super().__init__(nombre,edad,sexo,actividad)
   
    def hacer_actividad(self):
        print(f'Estoy estudiando: {self.actividad}')

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        super().__init__(nombre,edad,sexo,actividad)
   
    def hacer_actividad(self):
        print(f'Actualmente estoy trabajando en el rubro de: {self.actividad}')
    
ale = Estudiante('Alexis', 20, 'Masculino', 'Programacion')
mile = Trabajador('Jhamile', 20, 'Femenino', 'Medicina')

ale.presentarse()
ale.hacer_actividad()

mile.presentarse()
mile.hacer_actividad()
