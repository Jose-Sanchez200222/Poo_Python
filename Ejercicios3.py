
class Personajes():
    def __init__(self, nombre, fuerza, velocidad) -> None:
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
      
    #funcion de Representación en cadena del personaje.    
    def __repr__(self) -> str:
        return f'{self.nombre} (fuerza: {self.fuerza},velocidad: {self.velocidad})'
      
    #Función que permite la suma de dos personajes. Esta función define 
    # el comportamiento del operador + para objetos de la clase Personajes 
    def __add__(self, otro_pj):  
        nuevo_nombre = self.nombre + '_'+ otro_pj.nombre    
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza )/2)**2)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad )/2)**2)
        return Personajes(nuevo_nombre, nueva_fuerza, nueva_velocidad)  
    
goku = Personajes('Goku', 1000, 2000)   
vegeta = Personajes('Vegeta', 900, 1900)
jiren = Personajes('Jiren', 1200, 2100)

gogeta = goku + vegeta 
jireta = goku + vegeta + jiren
print(jireta)     