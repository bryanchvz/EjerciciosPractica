class Auto:
    def __init__(self,placa,modelo,problema):
        self.__placa = placa
        self.__modelo = modelo
        self.__problema = problema
        self.__reparado = False

    def get_placa(self):
        return self.__placa
    def get_modelo(self):
        return self.__modelo
    def get_problema(self):
        return self.__problema
    def get_reparado(self):
        return self.__reparado
    
    def set_placa(self,placa):
        self.__placa = placa
    def set_modelo(self,modelo):
        self.__modelo = modelo
    def set_problema(self,problema):
        self.__problema = problema
    def set_reparado(self,estado):
        self.__reparado = estado

    def marcar_reparado(self):
        self.__reparado = True
    
    
    def ver_autos(self):
        estado = "Reparado" if self.__reparado else "No_Reparado"
        print(f"Placa: {self.__placa}")
        print(f"Modelo: {self.__modelo}")
        print(f"Problema: {self.__problema}")
        print(f"Estado: {estado}")
        
autos = []
 
def ingresar_auto():
    placa = input("Ingrese la placa del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    problema = input("Que problema tiene su auto? ")
    nuevo = Auto(placa,modelo,problema)
    autos.append(nuevo)
    print("Auto ingresado con exito. ")
def ver_autos():
    placa = input("Ingrese la placa del auto que quiere ver: ")
    encontrado = False

    for a in autos:
        if a.get_placa() == placa:
            a.ver_autos()
            encontrado = True
            break
        else:
            if not encontrado:
                print("Auto no encontrado. o no existe.")   
def reparar_auto():
    placa = input("Ingrese la placa del auto que queire reparar: ")
    encontrado = False
    for auto in autos: 
        if auto.get_placa() == placa:
            encontrado = True
            auto.marcar_reparado()
            print("Auto marcado como reparado. ")
            break
        else:
            if not encontrado:
                print("Auto no encontrado: ")     

def guardar():
    try:
        with open("taller.txt","w", encoding= "utf-8") as archivo:
            for auto in autos:
                estado = "Reparado" if auto.get_reparado() else "No reparado"
                archivo.write(f"Placa: {auto.get_placa()} | Modelo: {auto.get_modelo()} | Problema: {auto.get_problema()} | Estado: {estado}\n")
                print("Guardado exitosamente")
    except Exception as e:
        print("Error al guardar {e}")
        
                              

while True:
    print("1. Ingresar auto")     
    print("2. Ver autos")     
    print("3. Reparar auto")
    print("4. Guardar en archivo taller.txt")
    print("5. Salir")

    opcion = input("Que opcion quieres ")

    if opcion == "1":
        ingresar_auto()
    elif opcion == "2":
        ver_autos()
    elif opcion =="3":
        reparar_auto()
    elif opcion == "4":
        guardar()
    elif opcion == "5":
        print("Saliendo")
        break
    else:
        print("no valido")    