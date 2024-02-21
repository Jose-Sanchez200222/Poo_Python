class Auto():
    def __init__(self) -> None:
        self._estado = 'apagado'
        pass
    
    def enceder(self):
        self._estado = 'encendido'
        print('El auto esta encendido')
        
    def conducir(self):
        if self._estado == 'apagado':
            self.enceder()
        print('Conduciendo  el auto')            
    
mi_auto = Auto()    
mi_auto.conducir()