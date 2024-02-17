class Persona:
    def __init__(self, nombre, edad, nacionalidad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad


    def hablar(self):
        print('hola, estoy hablando poco')
        pass
    
    
class Artista:
    def __init__(self, habilidad) -> None:
        self.habilidad = habilidad
        
    def mostrarHabilidad(self):
        print(f'mi habildad es: {self.habilidad}')
            
        pass    
    
class EmpleadoArtista(Persona,Artista): 
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa)  -> None:
        Persona().__init__(self, nombre, edad, nacionalidad)
        Artista().__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa