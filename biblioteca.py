class Libro:
    def __init__(self,id,titulo,autor):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True
    
    def get_id(self):
        return self.__id
    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor
    def get_disponible(self):
        return self.__disponible
    
    def set_id(self,id):
        self.__id = id
    def set_titulo(self,titulo):
        self.__titulo = titulo
    def set_autor(self,autor):
        self.__autor = autor
    def set_disponible(self,estado):
        self.__disponible = estado

    def ver_info(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        print(f"ID: {self.__id}")
        print(f"Titulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")
    
    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            print("Libro prestado con exito")
        else:
            print("El libro ya está prestado.")

    def devolver(self):
        if not self.__disponible:
            self.__disponible = True
            print("El libro ha sido devuelto con exito")
        else:
            print("El libro ya está disponible")


libros = []

def agregar_libro():
    id_libro = input("Ingrese la ID del libro que quiere agregar: ")
    titulo = input("Ingresa el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    nuevo = Libro(id_libro,titulo,autor)
    libros.append(nuevo)
    print("Libro agregado con exito")
def ver_libro():
    if not libros:
        print("No hay libros registrados. ")
        return
    for libro in libros:
        libro.ver_info()
    print()

def prestar_libro():
    id_buscado = input("Ingrese el ID del libro que quiere prestar: ")
    for libro in libros:
        if libro.get_id() == id_buscado:
            libro.prestar()
            return
    print("Libro no encontrado. ")

def devolver_libro():
    id_buscado = input("Ingrese el ID del libro a devolver. ")
    for libro in libros:
        if libro.get_id() == id_buscado:
            libro.devolver()
            return
    print("Libro no encontrado")

def guardar_catalogo():
    try:
        with open("catalogo.txt","w", encoding="utf-8") as archivo:
            for libro in libros:
                archivo.write(f"{libro.get_id()},{libro.get_titulo()},{libro.get_autor()},{libro.get_disponible()}\n")
                print("Catalogo guardado en 'catalogo.txt'. \n")
    except Exception as e:
        print(f"Error al guardar: {e}")

while True:
    print("1. Agregar libro")
    print("2. Ver libros")
    print("3. Prestar un libro (ID)")
    print("4. Devolver libro (ID)")
    print("5. Guardar el catalogo")
    print("6. Salir")

    opcion = input("Que opcion quieres: ")

    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        ver_libro()
    elif opcion =="3":
        prestar_libro()
    elif opcion == "4":
        devolver_libro()
    elif opcion == "5":
        guardar_catalogo()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida")