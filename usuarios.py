class Usuario:
    def __init__(self,id,nombre,email):
        self.__id = id
        self.__nombre = nombre
        self.__email = email
        self.__activo = False
    
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_email(self):
        return self.__email
    def get_activo(self):
        return self.__activo
    
    def set_id(self,id):
        self.__id = id
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_email(self,email):
        self.__email = email
    def set_activo(self,estado):
        self.__activo = estado
    
    def activar_usuario(self):
        self.__activo = True

    def desactivar_usuario(self):
        self.__activo = False
    
    def ver_info(self):
        estado = "Activo" if self.__activo else "No activo"
        print(f"ID: {self.__id}")
        print(f"Nombre: {self.__nombre}")
        print(f"Email: {self.__email}")
        print(f"Estado: {estado}")
        print("----------------")
usuarios = []

def agregar_usuario():
    id = input("Ingresa el ID: ")
    nombre = input("Ingresa el nombre de usuario: ")
    email = input("Ingresa el email: ")
    nuevo_usuario = Usuario(id,nombre,email)
    usuarios.append(nuevo_usuario)

    print("Usuario agregado con exito. ")
def ver_usuarios():
    if not usuarios:
        print("No hay usuarios registrados. ")
    else:
        for u in usuarios:
            u.ver_info()

def activar_usuario():
    id = input("Ingresa el ID del usuario a activar: ")
    encontrado = False

    for a in usuarios:
        if a.get_id() == id:
            encontrado = True
            a.activar_usuario()
            print("Usuario activado con exito.")
            break
    if not encontrado:
        print("Usuario no encontrado. ")

def desactivar_usuario():
    id = input("Ingresa el ID del usuario a desactivar: ")
    encontrado = False
    for a in usuarios:
        if a.get_id() == id:
            encontrado = True
            a.desactivar_usuario()
            print("Usuario desactivado con exito. ")
            break
    if not encontrado:
        print("Usuario no encontrado. ")

def guardar_usuarios():
    try:
        with open("usuarios.txt","w", encoding = "utf-8") as archivo:
            for u in usuarios:
                estado = "Activo" if u.get_activo() else "No Activo"
                archivo.write(f"ID: {u.get_id()} | Nombre: {u.get_nombre()} | Email: {u.get_email()} | Estado: {estado}\n")
                print("Usuario guardado exitosamente en: 'usuarios.txt' ")
    except Exception as e:
        print("Error al guardar {e}")

while True:
    print("------ Menu ------")
    print("1. Agregar usuario")
    print("2. Ver usuarios")
    print("3. Activar usuario")
    print("4. Desactivar usuario")
    print("5. Guardar usuarios en txt")
    print("6. Salir")

    opcion = input("Que opcion quieres? ")

    if opcion == "1":
        agregar_usuario()
    elif opcion == "2":
        ver_usuarios()
    elif opcion == "3":
        activar_usuario()
    elif opcion == "4":
        desactivar_usuario()
    elif opcion == "5":
        guardar_usuarios()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida")