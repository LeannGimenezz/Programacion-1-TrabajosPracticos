libros = [
    {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "año": 1605},
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967},
    {"titulo": "La Odisea", "autor": "Homero", "año": -800},
    {"titulo": "La Divina Comedia", "autor": "Dante Alighieri", "año": 1320},
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "año": 1615}
]

libros_ordenados_por_año = sorted(libros, key=lambda libro: libro["año"])
libros_ordenados_por_autor=sorted(libros, key=lambda libro: libro["autor"])
libros_ordenados_por_titulo=sorted(libros, key=lambda libro: libro["titulo"])


print(libros_ordenados_por_año)