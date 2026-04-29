class libro:
    def __init__(self,titulo,autor,ejemplares,stock):
        self.titulo=titulo
        self.autor=autor
        self.__ejemplares=ejemplares
        self.stock=stock
    
# @property
# def ejemplares(self):
#     return self.__ejemplares
# @ejemplares.setter
        

# @property
#     def nombre(self):
#         return self._nombre

#     @nombre.setter
#     def nombre(self, nuevo_nombre):
#         if len(nuevo_nombre) < 3:
#             print("Nombre demasiado corto")
#         else:
#             self._nombre = nuevo_nombre



class usuario:
    def __init__(self,nombre,id_usuario):
        self.libros_prestados=[]
        
        