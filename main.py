import time
import os


habitaciones_max = 50
habitaciones_disponibles = 50
historial = 0

print(f"\n¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!\n")
time.sleep(2)

while True:
    os.system("clear")    
    print(f"===MENÚ PRINCIPAL===")
    print(f"1. Habitaciones disponibles")
    print(f"2. Realizar Chek-in")
    print(f"3. Realizar Chek-out")
    print(f"4. Historial de ocupaciones")
    print(f"5. Salir")

    try:

        opcion = int(input("Elije una opción: "))

        if opcion == 1:
            print(f"Habitaciones disponibles: {habitaciones_disponibles}")

        elif opcion == 2:
            dato_valido = False
            while not dato_valido:
                try:
                    cantidad = int(input("¿Cuántas habitaciones desea reservar?: "))
                    if cantidad <= 0:
                        print("El número debe ser mayor a 0")
                    elif cantidad > habitaciones_disponibles:
                        print(f"No hay suficientes habitaciones. Disponibles: {habitaciones_disponibles}")
                    else:
                        dato_valido = True
                except:
                    print("Error, la cantidad está mal ingresada, ya que debe ser numérica.")

            habitaciones_disponibles -= cantidad
            historial                += cantidad
            print(f"Check-in realizado. Habitaciones reservadas: {cantidad}")

        elif opcion == 3:
            dato_valido = False
            while not dato_valido:
                try:
                    cantidad = int(input("¿Cuántas habitaciones desea liberar?: "))
                    if cantidad <= 0:
                        print("La cantidad debe ser mayor a 0")
                    elif cantidad > habitaciones_max:
                        print(f"No se pueden liberar más de {habitaciones_max} habitaciones.")
                    else:
                        dato_valido = True
                except:
                    print("Error, la cantidad está mal ingresada, ya que debe ser numérica.")

            habitaciones_disponibles += cantidad
            historial                -= cantidad
            print(f"Check-out realizado. Habitaciones liberadas: {cantidad}")

        elif opcion == 4:
            print(f"Total de ocupaciones registradas:{historial}")

        elif opcion == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            break
    
        else:
            print("Opción no válida: debes seleccionar un número entre el 1 y el 5.")
        
        time.sleep(2)

    except:
        print("ERROR: los datos están mal ingresados.")

