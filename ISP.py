from abc import ABC, abstractclassmethod

class Trabajador(ABC):
    
    @abstractclassmethod
    def trabajar(self):
        pass

 
class Comedor(ABC):    
    @abstractclassmethod
    def comer(self):
        pass
    
class Dormidor(ABC):     
    @abstractclassmethod
    def dormir(self):
        pass  
    
class Humano(Trabajador, Dormidor, Comedor):    
    
    def comer(self):
        print('El humano esta comiendo')
    
   
    def trabajar(self):
        print('El humano esta trabajando')
    
   
    def dormir(self):
        print('El humano esta durmiendo')
        
class Robot(Trabajador):    
    
    def trabajar(self):
        print('El robot esta trabajando')
        
robot = Robot() 
humano = Humano()


robot.trabajar()       
humano.comer()          