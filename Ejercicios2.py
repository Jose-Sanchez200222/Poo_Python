class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        pass
    
    def imprimirNE (self):
        print(f'Hola, soy: {self.nombre} y tengo {self.edad} ')
        pass
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado) -> None:
        super().__init__(nombre, edad)
        self.grado = grado
        pass
    
    def imprimirG(self):
        print(f'Me encuentro en el grado: {self.grado}')
        pass
      
alex = Estudiante('Alexis', 19, '3°')

alex.imprimirNE(), alex.imprimirG()

    