class persona:
    def __init__(self,nombre,edad,ciudad):
        self.nombre=nombre
        self.edad=edad
        self.ciudad=ciudad
        
    def presentarse(self):
       return f"hola me llamo {self.nombre} tengo {self.edad} y vivo en {self.ciudad}" 
        
    def mayor_edad(self):
        if self.edad > 18:
            print(" Si es mayor " )
            return True
        else:
            return False
    
    
per=persona("isacc",30,"babahoyo")
print(per.presentarse())
print(per.mayor_edad())

##asd###
print("\n-----segunda-------\n")

class rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return (self.base+ self.altura)*2
    
    def es_cuadrado(self):
        if self.base == self.altura:
            return True
        else:
            return False
cua=rectangulo(4,4)
print(cua.area())
print(cua.perimetro())
print(cua.es_cuadrado())
##asddsa#
print("\n-----tercera-------\n") 

class estudiante:
    def __init__(self,nombre,notas):
        self.nombre=nombre
        self.notas=notas 
        
    def promedio(self,x=0):
        self.x=x
        x=sum(self.notas)/len(self.notas)
        return 
    def aprobo(self):
        """lo logramos"""
        # def aprobo(self):
        # if self.promedio() > 60:
        #ia

        if self.x > 60:
            return True
        else:
            return False
    
    def nota_mas_alta(self):
        return  max(self.notas)
        
    def nota_mas_baja(self):
        return min(self.notas)


asd=estudiante("Pedrito", notas=[19,50,80,29])
asd.promedio()
print(asd.promedio())
asd.aprobo()
print(asd.aprobo())
print(asd.nota_mas_alta())
print(asd.nota_mas_baja())
#### siguiente parte
print("\n-----cuarta parte-------\n") 

    




        
        
        

    

        


        
    
    
        
        