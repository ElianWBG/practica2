def function():
    estudiantes = []   # lista para guardar estudiantes

    while True:
        print("\n--- MENU ---")
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Salir")

        opcion = input("Selecciona una opcion 1-4: ")

        if opcion == "1":
            nombre = input("Ingrese nombre del estudiante: ")
            estudiantes.append(nombre)
            print("Registro exitoso")

        elif opcion == "2":
            if estudiantes:
                print("Los estudiantes son:")
                for e in estudiantes:
                    print("-", e)
            else:
                print("No hay estudiantes registrados")

        elif opcion == "3":
            buscar = input("Nombre a buscar: ")
            if buscar in estudiantes:
                print("Estudiante encontrado")
            else:
                print("Estudiante no encontrado")

        elif opcion == "4":
            print("Saliendo del programa")
            break

        else:
            print("Opcion invalida")

# --- ESTA ES LA PARTE QUE FALTABA ---
# Llamamos a la función para que el código se ejecute
if __name__ == "__main__":
    function()