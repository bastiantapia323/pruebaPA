class Lote:
    def __init__(self, numero_lote, tamaño, precio, disponible=True):
        self.numero_lote = numero_lote
        self.tamaño = tamaño
        self.precio = precio
        self.disponible = disponible


class LoteosDuoc:
    def __init__(self):
        self.lotes = []  # Lista para almacenar los lotes
        self.clientes = []  # Lista para almacenar los clientes

    def ver_disponibilidad_lotes(self):
        for fila in range(5):  # Ejemplo: 5 filas de lotes
            for columna in range(5):  # Ejemplo: 5 columnas de lotes
                lote = self.lotes[fila][columna]
                if lote.disponible:
                    print(f"[ ]", end=" ")  # Espacio en blanco para lote disponible
                else:
                    print(f"[X]", end=" ")  # "X" para lote vendido
            print()  # Nueva línea para separar filas

    def seleccionar_lote(self):
        fila = int(input("Ingrese la fila del lote: "))
        columna = int(input("Ingrese la columna del lote: "))

        lote = self.lotes[fila][columna]
        if lote.disponible:
            rut = input("Ingrese su RUT: ")
            nombre = input("Ingrese su nombre completo: ")
            telefono = input("Ingrese su teléfono: ")
            email = input("Ingrese su email: ")

            cliente = {"RUT": rut, "Nombre": nombre, "Teléfono": telefono, "Email": email}
            lote.disponible = False
            self.clientes.append(cliente)
            print("¡Felicidades! Ha seleccionado el lote correctamente.")
        else:
            print("El lote seleccionado no está disponible. Por favor, elija otro lote.")

    def ver_detalles_lote(self):
        fila = int(input("Ingrese la fila del lote: "))
        columna = int(input("Ingrese la columna del lote: "))

        lote = self.lotes[fila][columna]
        print(f"Número de lote: {lote.numero_lote}")
        print(f"Tamaño del terreno: {lote.tamaño} m²")
        print(f"Precio: ${lote.precio}")

    def ver_clientes(self):
        if not self.clientes:
            print("Aún no hay clientes registrados.")
        else:
            print("Clientes que han comprado un lote:")
            for cliente in self.clientes:
                print(f"RUT: {cliente['RUT']}, Nombre: {cliente['Nombre']}")

    def iniciar_aplicacion(self):
        # Crear una matriz de lotes para el desarrollo residencial (ejemplo: 5x5)
        self.lotes = [[Lote(fila * 5 + columna, 200, 50000) for columna in range(5)] for fila in range(5)]

        while True:
            print("\n------ MENÚ ------")
            print("1. Ver disponibilidad de lotes")
            print("2. Seleccionar un lote")
            print("3. Ver detalles del lote seleccionado")
            print("4. Ver Clientes")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ver_disponibilidad_lotes()
            elif opcion == "2":
                self.seleccionar_lote()
            elif opcion == "3":
                self.ver_detalles_lote()
            elif opcion == "4":
                self.ver_clientes()
            elif opcion == "5":
                print("Gracias por usar la aplicación. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")


# Instanciar y ejecutar la aplicación
app = LoteosDuoc()
app.iniciar_aplicacion()