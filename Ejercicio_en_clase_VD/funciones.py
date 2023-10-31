def mostrar_menu():
    print("1 | AGREGAR PASAJEROS A LA LISTA")
    print("2 | AGREGAR CIUDADES A LA LISTA")
    print("3 | CONSULTA DE DESTINO (DNI)")
    print("4 | MOSTRAR LA CANTIDAD DE PASAJEROS QUE VIAJAN A LA CIUDAD")
    print("5 | MOSTRAR A QUE PAIS VIAJA")
    print("6 | MOSTRAR LA CANTIDAD DE PASAJEROS QUE VIAJAN AL PAIS")
    print("0 | SALIR DEL PROGRAMA")


def agregar_pasajeros():
    name=input("Ingrese el nombre del pasajero: ")
    dni=int(input("Ingrese el dni: "))
    city=input("Ingrese la ciudad de destino: ")
    country=input("Ingrese el pais de destino: ")

    tupla_ciudad = (city, country)

    return (name, dni, city, tupla_ciudad)