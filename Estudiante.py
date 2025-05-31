class Estudiante():
    def __init__(self,id,nombre,calificacion):
        self.__id = id
        self.__nombre = nombre
        self.__calificacion = calificacion
        self.__aprobado = calificacion >= 70
    
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_calificacion(self):
        return self.__calificacion
    def get_aprobado(self):
        return self.__aprobado
    
    def set_id(self,id):
        self.__id = id
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_calificacion(self,nueva_calificacion):
        self.__calificacion = nueva_calificacion
        self.__aprobado = nueva_calificacion >= 70
    
    def ver_info(self):
        estado = "Aprobado" if self.__aprobado else "Reprobado"
        print(f"ID: {self.__id}")
        print(f"Nombre: {self.__nombre}")
        print(f"Calificación: {self.__calificacion}")
        print(f"Estado: {estado}")


estudiantes = []
def agregar_estudiante():
    id = input("Ingresa el ID (matricula) del alumno: ")
    nombre = input("Ingresa el nombre del alumno: ")
    calificacion = int(input("Ingresa la calificacion del alumno (70 aprobado): "))
    nuevo = Estudiante(id,nombre,calificacion)
    estudiantes.append(nuevo)
    print("Estudiante agregado con exito")

def ver_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    for estudiante in estudiantes:
        estudiante.ver_info()
    print()

def guardar_estudiantes():
    try:
        with open("estudiantes.txt","w", encoding="utf-8") as archivo:
            for estudiante in estudiantes:
                archivo.write(f"{estudiante.get_id()},{estudiante.get_nombre()},{estudiante.get_calificacion()},{estudiante.get_aprobado()}\n")
                print("Estudiante guardado con exito en 'estudiantes.txt'.")
    except Exception as e:
        print(f"Error {e}")

while True:
    print("1. Agregar estudiante")
    print("2. Ver todos los estudiantes")
    print("3. Guardar estudiantes")
    print("4. Salir")
    
    opcion = input("que opcion quieres: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        ver_estudiantes()
    elif opcion == "3":
        guardar_estudiantes()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion invalida")