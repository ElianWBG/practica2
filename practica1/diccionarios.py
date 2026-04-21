class DiccionariosEjemplo:
    def ejecutar(self):

        # =========================
        # CREACIÓN
        # =========================
        print("=== CREACIÓN ===")

        persona = {
            "nombre": "Juan",
            "edad": 25,
            "ciudad": "Guayaquil",
            "hobbies": ["música", "deportes"]
        }

        print(persona)

        # =========================
        # ACCESO
        # =========================
        print("\n=== ACCESO ===")

        print(persona["nombre"])
        print(persona["hobbies"][0])

        # =========================
        # GET (SEGURO)
        # =========================
        print("\n=== GET ===")

        print(persona.get("telefono", "No disponible"))

        # =========================
        # MODIFICAR
        # =========================
        print("\n=== MODIFICAR ===")

        persona["edad"] = 26
        print(persona)

        # =========================
        # AGREGAR
        # =========================
        print("\n=== AGREGAR ===")

        persona["telefono"] = "0991234567"
        print(persona)

        # =========================
        # ELIMINAR
        # =========================
        print("\n=== ELIMINAR ===")

        del persona["telefono"]
        print(persona)

        # =========================
        # MÉTODOS
        # =========================
        print("\n=== MÉTODOS ===")

        print("Claves:", list(persona.keys()))
        print("Valores:", list(persona.values()))
        print("Items:", list(persona.items()))

        # =========================
        # EXISTENCIA
        # =========================
        print("\n=== EXISTENCIA ===")

        print("nombre" in persona)
        print("apellido" in persona)

        # =========================
        # COMBINAR
        # =========================
        print("\n=== COMBINAR ===")

        extra = {
            "apellido": "Pérez",
            "profesion": "Ingeniero"
        }

        persona.update(extra)
        print(persona)

        # =========================
        # COMPRENSIÓN
        # =========================
        print("\n=== COMPRENSIÓN ===")

        cuadrados = {x: x**2 for x in range(5)}
        print(cuadrados)

        # =========================
        # COPIAR
        # =========================
        print("\n=== COPY ===")

        copia = persona.copy()
        print(copia)

        # =========================
        # CLEAR
        # =========================
        print("\n=== CLEAR ===")

        copia.clear()
        print(copia)

        # =========================
        # DICCIONARIO ANIDADO
        # =========================
        print("\n=== ANIDADO ===")

        universidad = {
            "estudiante": {
                "nombre": "María",
                "edad": 20
            },
            "profesor": {
                "nombre": "Carlos",
                "materia": "Programación"
            }
        }

        print(universidad["estudiante"]["nombre"])

        # =========================
        # EJERCICIO 1
        # =========================
        print("\n=== EJERCICIO 1 ===")

        datos = {"a": 1, "b": 2}
        print(datos["a"])

        # =========================
        # EJERCICIO 2
        # =========================
        print("\n=== EJERCICIO 2 ===")

        datos = {"x": 10}
        print(datos.get("y", "No existe"))

        # =========================
        # EJERCICIO 3 (ANÁLISIS)
        # =========================
        print("\n=== EJERCICIO 3 ===")

        datos = {"a": 1}
        copia = datos
        copia["b"] = 2

        print(datos)
        print(copia)
objeto_dic = DiccionariosEjemplo()
objeto_dic.ejecutar()        