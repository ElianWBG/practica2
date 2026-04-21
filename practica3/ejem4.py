class producto:
    def __init__(self,nombre,precio,stock):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
    def mostrar_info(self):
        print(f"producto:{self.nombre}. precio:{self.precio} .stock {self.stock} " )
  
    def esta_disponible(self):
        if self.stock > 0:
            print("True")
        else:
            print("False")    
        return
p=producto("manzana",49,10)
pa=producto("pera",423,14)
print(p.mostrar_info())
print(pa.esta_disponible())
print(p.__dict__)