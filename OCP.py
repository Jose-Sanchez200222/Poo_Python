class Notficador:
    def __init__(self, usuario, mensaje) -> None:
        self.usuario = usuario
        self.mensaje = mensaje
        pass
    
    def modificar(self):
        raise NotImplemented#para agregar funciones y tener todo lo importante
    
    
class NotificadorEmail(Notficador):
    def Notificar(self):
        print(f'Enviamos el mensaje a {self.usuario.email}')    
        
class NotificadorSMS(Notficador):
    def Notificar(self):
        print(f'Enviamos SMS a {self.usuario.sms}')           
                
class NotificadorWhatssap(Notficador):
    def Notificar(self):
        print(f'Enviamos por Whatssap a {self.usuario.whatssap}')  
                
class NotificadorTwiter(Notficador):
    def Notificar(self):
        print(f'Enviamos Twiter a {self.usuario.twiter}')  