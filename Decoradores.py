def decorador(funcion):
    def funcion_modificada():
        print('Antes de llamar a la funcion ')
        funcion()
    return funcion_modificada
    
# def saludo():
#     print('Hola Lexis')    
    
# saludo_modificado = decorador(saludo)    
# saludo_modificado()

@decorador#forma optima 
def saludo():
    print('Hola Lexis')
    
saludo()    