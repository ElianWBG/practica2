def validar_condicion(Notificar_gerente):
    def validar_nuevamente():
        print("Validando la condición...")
        Notificar_gerente()
        print("Condición validada. Notificando al gerente...")
    return validar_nuevamente
@validar_condicion
def Notificar_gerente():
    print("¡Gerente notificado! 🚨")

      
          
   
@validar_condicion
class equipo_Fut():
    def __init__(self,nombre_Equipo,Plantilla,Escudo,Valor_Equipo):
        self.nombre=nombre_Equipo
        self.plantilla=Plantilla
        self.escudo=Escudo
        self.valor=Valor_Equipo
        def mostrar_Equipo(self):
            print(f"El equipo {self.nombre} tiene una plantilla de {self.plantilla} jugadores, su escudo es {self.escudo} y su valor es de {self.valor} millones de euros.")    
        def enternar(self):
            print(f"El equipo {self.nombre} está entrenando para el próximo partido.")                            
        
@validar_condicion     
class jugador_Fut():
    def __init__(self,nombre_Jugador,Posicion,Valor_Jugador):
        self.nombre=nombre_Jugador
        self.posicion=Posicion
        self.valor=Valor_Jugador
        def mostrar_Jugador(self):
            print(f"El jugador {self.nombre} juega en la posición de {self.posicion} y su valor es de {self.valor} millones de euros.")
        def entrenar(self):
            print(f"El jugador {self.nombre} está entrenando para mejorar su rendimiento.")
            if self.valor > 100:
                print(f"¡El jugador {self.nombre} es una estrella!")
        
        
        
@validar_condicion      
class entrenador_Fut():
    
    
    def __init__(self,nombre_Entrenador,Valor_Entrenador):
        self.nombre=nombre_Entrenador
        self.valor=Valor_Entrenador
        
@validar_condicion       
class estadio_Fut():  
    def __init__(self,nombre_Estadio,Capacidad,Valor_Estadio):
        self.nombre=nombre_Estadio
        self.capacidad=Capacidad
        self.valor=Valor_Estadio
        
        
class sponsor_Fut(equipo_Fut,jugador_Fut,entrenador_Fut,estadio_Fut):
    def __init__(self,nombre_Sponsor,Valor_Sponsor):
        self.nombre=nombre_Sponsor
        self.valor=Valor_Sponsor
        
print("Ejemplo de uso:")
equipo1 = equipo_Fut("Barcelona", 25, "Escudo del Barcelona", 1000)
jugador1 = jugador_Fut("Lionel Messi", "Delantero", 150)
entrenador1 = entrenador_Fut("Xavi Hernández", 50)          
estadio1 = estadio_Fut("Camp Nou", 99354, 500)
sponsor1 = sponsor_Fut("Nike", 200) 
