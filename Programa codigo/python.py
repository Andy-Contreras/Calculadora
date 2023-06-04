from menu import principal
import os
import time

var = principal()
lista = ["1)Suma ","2)Resta","3)Multiplicación","4)División","5)Conversiones"]
opcion = ""
while opcion != 5:
    os.system("cls")
    opcion = var.menu(lista)
    if opcion ==  "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        suma = num1 + num2
        resultado = suma
        print("El resultado es:", resultado)
        time.sleep(1)

    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resta = num1 - num2
        resultado = resta
        print("El resultado es:", resultado)
        time.sleep(1)

    elif opcion == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        multiplicacion = num1 * num2
        resultado = multiplicacion
        print("El resultado es:", resultado)
        time.sleep(1)

    elif opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        division = num1 / num2
        resultado = division
        print("El resultado es:", resultado)
        time.sleep(1)

    elif opcion == "5":
        numero = input("Ingrese un número: ")
        base_actual = int(input("Ingrese la base del sistema numérico actual: "))
        base_objetivo = int(input("Ingrese la base del sistema numérico objetivo: "))
        resultado = conversion_sistemas(numero, base_actual, base_objetivo)
        print("El número convertido es:", resultado)
        time.sleep(1)

    elif opcion == "6":
        print("Opcion invalidad ingrese las opciones que tiene")
        time.sleep(1)

print("Gracias por visitarnos")
