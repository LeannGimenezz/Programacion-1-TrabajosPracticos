#Pidiendo la fecha al usuario, en formato dia, DD/MM
date = input("Ingrese la fecha actual en formato dia, DD/MM: ")

#Separando los datos que voy a utilizar insetandolos en una lista
date_list = date.split(",")
#Obtengo el dia y lo convierto a minuscula
day = date_list[0].lower()

#Separo DD/MM en dia y mes
day_month=date_list[1].split("/")

#Obtengo el DD, y le quito el espacio de adelante
day_number=int(day_month[0].strip())

#Obtengo el MM
month = int(day_month[1])

days = ["lunes","martes","miercoles","jueves","viernes"]
index_day = days.index(day)

if day in days and day_number<32 and day_number>0 and month>00 and month<13:
    if index_day<3:
        decision= input("Se tomaron examenes? (Presione y para si, n para no): ").lower()
        if decision == "y":
            passed = int(input("Ingrese cuantos alumnos aprobaron: "))
            not_passed = int(input("Ingrese cuantos alumnos desaprobaron: "))
            porcentaje = round((passed *100 )/(passed + not_passed),2)
            print(f"El porcentaje de alumnos aprobados es: %{porcentaje}")
    elif index_day == 3:
        asistance=int(input("Ingrese el numero del porcentaje de asistencia: ")) 
        if asistance>50:
            print("Asistio la mayoria")     
        else: 
            print("No asistio la mayoria")
    else:
        if (day_number == 1 and month == 1) or (day_number == 1 and month == 7):
            print("Comienzo nuevo ciclo")
            cant_students = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            payment_per_student = int(input("Ingrese el arancel por alumno: "))
            print(f"El ingreso total es de: ${cant_students*payment_per_student}" )
        else:
            print("Se esta cursando un ciclo actualmente")
            
else:       
    print("ERROR")




