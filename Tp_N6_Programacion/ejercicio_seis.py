
alumnos_primario = list()
alumnos_secundario = list()

nombre = ""
print("CARGANDO LOS ALUMNOS DE PRIMARIA...")
while(nombre != "x"):
    nombre = input("Ingrese un nombre: ").lower()
    if(nombre != "x"):
        alumnos_primario.append(nombre)
    else:
        print("SE HAN CARGADO CORRECTAMENTE LOS ALUMNOS DE PRIMARIA")
        break
    
nombre = ""   
print("CARGANDO LOS ALUMNOS DE SECUNDARIA...")
    
while(nombre != "x"):
    nombre = input("Ingrese un nombre: ").lower()
    if(nombre != "x"):
        alumnos_secundario.append(nombre)
    else:
        print("SE HAN CARGADO CORRECTAMENTE LOS ALUMNOS DE SECUNDARIA")
        break
    
todos_los_alumnos = set(alumnos_primario) | set(alumnos_secundario)
print("Los nombres de todos los alumnos son:")
for nombre in todos_los_alumnos:
    print(nombre)
    
alumnos_repetidos = set(alumnos_primario) & set(alumnos_secundario)
print("Los siguientes nombres se repiten entre los alumnos de nivel primario y secundario:")
for nombre in alumnos_repetidos:
    print(nombre)  
    
alumnos_primario_no_repetidos = set(alumnos_primario) - set(alumnos_secundario)
print("Los siguientes nombres no se repiten entre los alumnos de nivel primario y secundario:")
for nombre in alumnos_primario_no_repetidos:
    print(nombre)
