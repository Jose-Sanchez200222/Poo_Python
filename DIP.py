# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #Logica para verificar las palabras
#         pass
    
    
# class CorrectorOrtografico:
#     def __init__(self) -> None:
#         self.diccionario = Diccionario()
#         pass    
    
#     def corregir_texto(self, texto):
#         #usamos el dicionario para coregir el texto
#         pass

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificador_palabra(self, palabra):
       
        pass
    
class Diccionario(VerificadorOrtografico):    
    def verificador_palabra(self, palabra):
        #logica para verificar palabras si esta en el dicionario
        pass
    
# class ServicioOneline(VerificadorOrtografico):
#     def verificador_palabra(self, palabra):
#         #logica para verificar la palbara desde la web
#         pass
    
class CorrectorOrtografico():
    def __init__(self, verificador) -> None:
        self.verificador = verificador
        pass    
    
    def corregir_texto(self, texto):
        #usamos el verificador para corregir el texto
        pass

corrector = CorrectorOrtografico(Diccionario())