class Celular: #clase
    def __init__(self, marca, modelo,  camara: int) -> None:
        self.marca = marca + '\tNuevo'
        self.modelo = modelo
        self.camara = f'{camara} \tMP'
        
    def llamar(self): #metodos
        print(f'estas haciendo un llamada desde un : {self.modelo}')
            
    def cortar(self):
        print(f'estas cortando la llamada desde tu: {self.modelo}')       
        
        pass
    
celualar1 = Celular('samsung', 's23', 48) #objeto

celualar2 = Celular('apple', '16pro', 64) 

celualar2.cortar()   # llamar al objeto
    
