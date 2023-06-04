import os
os.system("cls")
class principal:
    def __init__(self):
        pass
    def menu(self,opciones):
        print("Menu de Calculadora")
        for opcion in opciones: 
            print(opcion)
        opc = input("Elija opcion[1...{}] : " .format(len(opciones)))
        return opc 