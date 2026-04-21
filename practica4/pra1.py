class universidad:
    def __init__(self,nombre,ubicacion,carrera,precio):
        self.nombre=nombre
        self.ubicacion=ubicacion
        self.carreras=carrera
        self.precio=precio
        
def evaluacion(Notificar_estado):
    def evaluacion_final():
        print("previo a la visita")
        Notificar_estado()
        print("Visita realizada")
    return evaluacion_final
@evaluacion
def Notificar_estado()
# def validar_condicion(Notificar_gerente):
#     def validar_nuevamente():
#         print("Validando la condición...")
#         Notificar_gerente()
#         print("Condición validada. Notificando al gerente...")
#     return validar_nuevamente
# @validar_condicion
# def Notificar_gerente():
#     print("¡Gerente notificado! 🚨")


    
            
        
    def mostrar_nombre(self):
        print(f"La {self.nombre} se ubica en {self.ubicacion} ")
        return 
estudiantes=universidad("unemu",40234.3123,"ing de sofware",40231)
estudiantes.mostrar_nombre()