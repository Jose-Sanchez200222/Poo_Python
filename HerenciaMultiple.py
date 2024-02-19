class Persona:
    def __init__(self, nombre, edad, nacionalidad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print('hola, estoy hablando poco')

class Artista:
    def __init__(self, habilidad) -> None:
        self.habilidad = habilidad

    def mostrarHabilidad(self):
        return f'mi habildad es: {self.habilidad}'

class EmpleadoArtista(Persona, Artista): #herencia multiple
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario) -> None:
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.empresa = empresa
        self.salario = salario

    def presentarse(self):
        print (f'Hola, soy : {self.nombre}, {self.mostrarHabilidad()} y trabajo en {self.empresa}')#tambien se puede remplazar por self solo de la clase metodo reescrito , super siempre de la clase padre

alexis = EmpleadoArtista('Alexis', 19, 'Peruano', 'Programar', 'DevSecurity', 100)

herencia = issubclass(EmpleadoArtista,Artista)#para saber de que clase hereda
isinstance = isinstance(alexis,EmpleadoArtista)#verifica la istancia del objeto

print(isinstance)
