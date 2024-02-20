class Animal: #polimorfismo con herencia
    def sonido(self):
        pass
    
class Gato(Animal):#sin colocar la herencia funciona en lenguajes dinamicos
    def sonido(self):
        return 'Miau'
    
class Perro(Animal):
    def sonido(self):
        return 'Guau' 
    
def hacer_sonido(animal):       
    print(animal.sonido())
    
gato = Gato()
perro = Perro()

print(perro.sonido())
hacer_sonido(gato)

#poliformisfo nativo en python
def recorrer(elemento):
    for item in elemento:
        print(f'El elmwnto es {item}')
        
lista = [1,2,3,4]
lista2 = 'Security'

recorrer(lista2)        

# DUCK TYPING
# donde el tipo de un objeto se determina por sus habilidades 
# (métodos y atributos) en lugar de su clase explícita. 
# En otras palabras, 
# "si camina como un pato y grazna como un pato, entonces es un pato" 
# sin importar de qué clase específica provenga.