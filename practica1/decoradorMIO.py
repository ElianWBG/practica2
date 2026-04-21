# # 1. Definimos el "superpoder" (el decorador)
# def decorador_limpieza(funcion_original):
#     def envoltorio():
#         print("🧼 Lavándose las manos...") # Lo que pasa antes
#         funcion_original()                 # La acción principal
#         print("🧽 Lavando los platos...")  # Lo que pasa después
#     return envoltorio

# # 2. Se lo ponemos a nuestra función
# @decorador_limpieza
# def cocinar():
#     print("🍝 Cocinando pasta deliciosa")

# # 3. Al llamar a cocinar(), se activan los superpoderes
# cocinar()

def funcion_a(funcion_b):
    def funcion_c():
        print("primera parte pa")
        funcion_b()
        print("segunda parte pa")
    return funcion_c

@funcion_a
def permitir():
    print("media parte pa")
permitir()        
##otro ejemplo
#
#
#
#
def registrar_accion(funcion):
    def envoltorio():
        print(f"--- LOG: Se intentó ejecutar la función: {funcion.__name__} ---")
        return funcion()
    return envoltorio

@registrar_accion
def realizar_pago():
    print("Pago procesado con éxito. 💰")

realizar_pago()    