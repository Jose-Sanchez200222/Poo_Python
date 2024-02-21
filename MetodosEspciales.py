class Persona:
    def __init__(self, nombre, edad) -> None:#__init__ metodo especial
        self.nombre = nombre 
        self.edad = edad
        pass
    
    def __str__(self) -> str: # como mostrarse en cadena de texto , lista
        return f'Persona(nombre={self.nombre},edad={self.edad})'
        
    def __repr__(self) -> str:
        return f'Persona("{self.nombre}",{self.edad})'#siempre entre comillas
     
    def __add__(self, otro):#comportamiento de la suma (+) / sobrecarga de operadores
        nuevo_valor = self.edad + otro.edad    
        return Persona(self.nombre+otro.nombre,nuevo_valor)
        
ale = Persona('Alexis', 19)
mile = Persona('Jhamile', 20)
cielo = Persona('Maricyelo', 18)

# repre = repr(ale)#representacion del objeto
# resultado = eval(repre)#reconstruyo el objeto

nueva_persona = ale + mile + cielo#suma de objetos
print(nueva_persona.nombre)        

# lista = (1,2,3,4)#la lista tambien funciona como objeto
# print(lista)
    