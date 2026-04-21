class TuplasEjemplo:
    def ejecutar(self):

        # =========================
        # CREACIÓN DE TUPLAS
        # =========================
        print("=== CREACIÓN ===")

        tupla1 = (1, 2, 3, 4, 5)
        tupla2 = (6, "python", True, 3.14)

        print(tupla1)
        print(tupla2)

        # =========================
        # CONCATENACIÓN
        # =========================
        print("\n=== CONCATENACIÓN ===")

        concatenada = tupla1 + tupla2
        print(concatenada)

        # =========================
        # REPETICIÓN
        # =========================
        print("\n=== REPETICIÓN ===")

        repetida = tupla1 * 2
        print(repetida)

        # =========================
        # ACCESO
        # =========================
        print("\n=== ACCESO ===")

        print(tupla1[0])
        print(tupla1[-1])

        # =========================
        # SLICING
        # =========================
        print("\n=== SLICING ===")

        print(tupla1[1:4])
        print(tupla1[:3])
        print(tupla1[-3:])

        # =========================
        # FUNCIONES
        # =========================
        print("\n=== FUNCIONES ===")

        print(len(tupla2))
        print(max(tupla1))
        print(min(tupla1))

        # =========================
        # MÉTODOS
        # =========================
        print("\n=== MÉTODOS ===")

        numeros = (10, 5, 8, 1, 9, 3, 5, 5)

        print(numeros.count(5))
        print(numeros.index(5))

        # =========================
        # PERTENENCIA
        # =========================
        print("\n=== PERTENENCIA ===")

        print(3 in tupla1)
        print(7 not in tupla1)

        # =========================
        # CONVERSIÓN
        # =========================
        print("\n=== CONVERSIÓN ===")

        lista_temp = list(tupla1)
        lista_temp.append(6)

        nueva_tupla = tuple(lista_temp)
        print(nueva_tupla)

        # =========================
        # DESEMPAQUETADO
        # =========================
        print("\n=== UNPACKING ===")

        a, b, c, d = (1, 2, 3, 4)
        print(a, b, c, d)

        # =========================
        # UNPACKING CON *
        # =========================
        print("\n=== UNPACKING CON * ===")

        primero, *resto, ultimo = (1, 2, 3, 4, 5)

        print("Primero:", primero)
        print("Resto:", resto)
        print("Último:", ultimo)

        # =========================
        # TUPLAS ANIDADAS
        # =========================
        print("\n=== ANIDADAS ===")

        tupla_anidada = (1, (2, 3), (4, 5, 6))

        print(tupla_anidada[1][1])

        # =========================
        # EJERCICIO 1
        # =========================
        print("\n=== EJERCICIO 1 ===")

        tupla = (1, 2, 3)
        print(tupla[1])

        # =========================
        # EJERCICIO 2
        # =========================
        print("\n=== EJERCICIO 2 ===")

        tupla = (10, 20, 30, 40)
        print(tupla[1:3])

        # =========================
        # EJERCICIO 3 (ANÁLISIS)
        # =========================
        print("\n=== EJERCICIO 3 ===")

        tupla = (1, 2, 3)
        # tupla[0] = 10  # ¿Qué error genera?
objeto_tuplas = TuplasEjemplo()
objeto_tuplas.ejecutar()        