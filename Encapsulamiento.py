class MiClase:
    def __init__(self) -> None:
        self.__atributo_privado = 'valor'#Atributo privado '_', muy privado '__'
        pass
    
    def __hablar():#metodos privados
        print('Hola como estas ')
    
objeto = MiClase()
print(objeto.__atributo_privado)    
    