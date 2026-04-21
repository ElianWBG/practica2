# def function():
#     vehiculos=[]
    
#     while True:
#         print("\n---MENU----\n")
#         print("registrar nombre del vehiculo")
#         print("Buscar vehiculo")
#         print("Salir")
#         opcion=input("Ingrese una opcion del 1-3 "  )
#         if opcion == "1":
#             while True:
#                 nombre = input("Ingrese nombre del vehiculo ").strip()
#                 valor=input("Ingrese valor del vehiculo").strip()  
                
#                 if valor.replace(" ", "").isdigit():
#                     vehiculos.append(valor)
#                     print("valor registrado con exito")
#                     break
#                 else:
#                     print("hubo un error al ingresar el valor " )
                    
#                 if nombre.replace(" ", "").isalpha():
#                     vehiculos.append(nombre)
#                     print("Registro exitoso")
#                     break
#                 else:
#                     print(" Error: El nombre solo debe contener letras y no puede estar vacío. ")
#                     break
#         elif opcion=="2":
#             buscar=input("Ingrese el vehiculo a buscar ")
#             if buscar in vehiculos:
#                 print(" vehiculo encontrado " )
#             else:
#                 print(" vehiculo no encontrado pa " )
#         elif opcion=="3":
#             print("saliendo del programa")
#             break
            
# if __name__=="__main__":
#     function()    
def function():
    vehiculos = []   # Aquí guardaremos el formato "Nombre - Valor"
    
    while True:
        print("\n--- MENU ---")
        print("1. Registrar vehículo")
        print("2. Buscar vehículo")
        print("3. Salir")
        
        opcion = input("Ingrese una opcion del 1-3: ")

        if opcion == "1":
            while True:
                nombre = input("Ingrese nombre del vehiculo: ").strip()
                # 1. Validamos nombre
                if nombre.replace(" ", "").isalpha() and nombre != "":
                    
                    # 2. Si el nombre es correcto, pedimos el valor
                    while True:
                        valor = input(f"Ingrese valor para {nombre}: ").strip()
                        if valor.isdigit():
                            # Guardamos ambos datos en una sola cadena para que sea fácil buscar
                            registro = f"{nombre} (Precio: {valor})"
                            vehiculos.append(registro)
                            print("¡Registro exitoso!")
                            break # Sale del bucle del valor
                        else:
                            print("Error: El valor debe ser solo números.")
                    
                    break # Sale del bucle del nombre y vuelve al menú
                else:
                    print("Error: El nombre debe contener solo letras.")

        elif opcion == "2":
            buscar = input("Ingrese el nombre del vehiculo a buscar: ").strip()
            encontrado = False
            
            for v in vehiculos:
                # Comprobamos si el nombre que escribió el usuario está dentro de nuestros registros
                if buscar.lower() in v.lower():
                    print(f"Vehículo encontrado: {v}")
                    encontrado = True
                    break
            
            if not encontrado:
                print("Vehículo no encontrado, pa.")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

if __name__=="__main__":
    function()