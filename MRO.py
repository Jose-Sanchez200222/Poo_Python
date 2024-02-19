class A:
    def hablar(self):
        print('Hola desde A')
    pass

class F(A):
    def hablar(self):
        print('Hola desde F')
    pass    
        
class B(A):
    # def hablar(self):
    #     print('Hola desde B')
    pass
        
class C(F):
    # def hablar(self):
    #     print('Hola desde C')
    pass
                        
class D(B,C):
    # def hablar(self):
    #     print('Hola desde D')   
    pass       
        
        
d = D()

print(D.mro()) #para ver el orden de heredar
# d.hablar()                      