class Animal:
    def comer(self):
        print('El animal esta comiendo...')
        pass

class Mamifero(Animal):
    def amamantar(self):
        print('El animal esta amamantando ')  
        pass  
        
class Ave(Animal):
    def volar(self):
        print('El animal esta volando ') 
        pass
        
class Murcielago(Mamifero,Ave): 
    pass

murcielago = Murcielago()
murcielago.amamantar(),murcielago.volar(),murcielago.comer()

# print(Murcielago.mro())              