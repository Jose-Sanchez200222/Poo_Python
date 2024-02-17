class Estudiante:
    def __init__(self, nombre, edad:int, grado:int) -> None:
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
     
    def estudiar(self): 
        estudiando = input('Que desea haer? ').lower()
        if estudiando == 'estudiar':
            print(f'el estudiante {self.nombre} esta estudiando')  
        else:
            print("Acción no válida")
             
        pass
    
Estudiante1 = Estudiante(input("Ingrese su nombre: "), int(input("Ingrese su edad: ")), int(input("Ingrese su grado: ")))  


Estudiante1.estudiar()  

print(f"""
      ---Datos del estudiante---
      \nNombre: {Estudiante1.nombre}
      \nEdad: {Estudiante1.edad}
      \nGrado: {Estudiante1.grado}
      """)
