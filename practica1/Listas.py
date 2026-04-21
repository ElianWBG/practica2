class ListasEjemplo:
    def ejecutar(self):

        # =========================
        # CREACIÓN DE LISTAS
        # =========================
        print("=== CREACIÓN ===")

        lista1 = [1, 2, 3, 4, 5]
        lista2 = [6, 7, 8, 9, 10]
        numeros = [10, 5, 8, 1, 9, 3]

        print(lista1)
        print(lista2)

        # =========================
        # CONCATENACIÓN
        # =========================
        print("\n=== CONCATENACIÓN ===")

        concatenada = lista1 + lista2
        print(concatenada)

        # =========================
        # FUNCIONES BÁSICAS
        # =========================
        print("\n=== FUNCIONES ===")

        print("Suma:", sum(lista1))
        print("Máximo:", max(numeros))
        print("Mínimo:", min(numeros))

        # =========================
        # ORDENAMIENTO
        # =========================
        print("\n=== ORDENAMIENTO ===")

        print("Ordenado (nuevo):", sorted(numeros))

        numeros.sort(reverse=True)
        print("Ordenado descendente:", numeros)

        # =========================
        # INVERTIR
        # =========================
        print("\n=== REVERSE ===")

        lista1.reverse()
        print(lista1)

        # =========================
        # CONTAR
        # =========================
        print("\n=== COUNT ===")

        lista_repetidos = [1, 2, 2, 3, 3, 3]
        print(lista_repetidos.count(3))

        # =========================
        # COPIAR
        # =========================
        print("\n=== COPY ===")

        copia = lista1.copy()
        print(copia)

        # =========================
        # EXTENDER
        # =========================
        print("\n=== EXTEND ===")

        lista1.extend([6, 7, 8])
        print(lista1)

        # =========================
        # INSERTAR
        # =========================
        print("\n=== INSERT ===")

        lista2.insert(2, 100)
        print(lista2)

        # =========================
        # POP
        # =========================
        print("\n=== POP ===")

        eliminado = lista2.pop()
        print("Eliminado:", eliminado)
        print(lista2)

        # =========================
        # REMOVE
        # =========================
        print("\n=== REMOVE ===")

        lista2.remove(100)
        print(lista2)

        # =========================
        # CLEAR
        # =========================
        print("\n=== CLEAR ===")

        lista2.clear()
        print(lista2)

        # =========================
        # EJERCICIO 1
        # =========================
        print("\n=== EJERCICIO 1 ===")

        lista = [3, 1, 4, 1, 5]
        print(sorted(lista))

        # =========================
        # EJERCICIO 2
        # =========================
        print("\n=== EJERCICIO 2 ===")

        lista = [10, 20, 30]
        lista.append(40)
        print(lista)

        # =========================
        # EJERCICIO 3 (ANÁLISIS)
        # =========================
        print("\n=== EJERCICIO 3 ===")

        lista = [1, 2, 3]
        copia = lista
        copia.append(4)

        print(lista)
        print(copia)
objeto_listas = ListasEjemplo()
objeto_listas.ejecutar()        