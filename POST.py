class Post:
    def __init__(self,id_post,mensaje,autor):
        self.__id_post = id_post
        self.__mensaje = mensaje
        self.__autor = autor
        self.__vistas = 0
        self.__likes = 0
    
    def get_id_post(self):
        return self.__id_post
    
    def get_mensaje(self):
        return self.__mensaje
    
    def get_autor(self):
        return self.__autor
    
    def get_vistas(self):
        return self.__vistas
    
    def get_likes(self):
        return self.__likes
    
    def set_mensaje(self,mensaje):
        self.__mensaje = mensaje
    
    def set_autor(self,autor):
        self.__autor = autor
    
    def ver_post(self):
        self.__vistas += 1
        print(f"ID: {self.__id_post}")
        print(f"Mensaje: {self.__mensaje}")
        print(f"Autor: {self.__autor}")
        print(f"Likes: {self.__like}")
        print(f"Vistas: {self.__vistas}")
    
    def dar_like(self):
        self.__like += 1

publicaciones = []

def agregar_publicaciones():
    id_post = input("Ingrese la clave del post: ")
    mensaje = input("Ingrese el mensaje de post: ")
    autor = input("Ingresa el autor del post: ")
    nuevo_post = Post(id_post,mensaje,autor)

    publicaciones.append(nuevo_post)
    print("Post agregado!")

def ver_post():
    clave = input("Ingrese la clave del post que quieres buscar: ")
    encontrado = False

    for post in publicaciones:
        if post.get_id_post() == clave:
            post.ver_post()
            encontrado = True
            break
        if not encontrado:
            print("Publicacion no encontrada. ")

def ver_likes():
    clave = input("Ingrese la clave del post que le quiere dar like: ")
    encontrado = False

    for post in publicaciones:
        if post.get_id_post() == clave:
            post.dar_like()
            print("Like agregado :) ")
            encontrado = True
            break
        if not encontrado: 
            print("Publicacion no encontrada. ")

def respaldar_post():
    try:
        with open("prueba.txt", "w", encoding= "utf-8") as archivo:
            for post in publicaciones:
                archivo.write(f"{post.get_id_post()},{post.get_mensaje()},{post.get_autor()},{post.get_vistas()},{post.get_likes()}\n")
        print("Publicaciones respaldadas en 'prueba.txt'\n")
    except Exception as e:
        print(f"Error al respaldar {e}\n")

while True:
    print("1. Agregar post")
    print("2. Ver post")
    print("3. Ver likes")
    print("4. Respaldar Publicaciones")
    print("5. Salir")
    
    opcion = input("¿Que quiere hacer? ")

    if opcion == "1":
        agregar_publicaciones()
    elif opcion == "2":
        ver_post()
    elif opcion == "3":
        ver_likes()
    elif opcion == "4":
        respaldar_post()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción invalida")