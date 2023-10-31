def recorrer_carton(num, carton):
    for i in range(len(carton)):
        if(num in carton[i]):
            return False
        else:
            return True
            
def eliminar_numero(bola, carton):
    for i in range(len(carton)):
        if(bola in carton[i]):
            carton[i].remove(bola)
            print(f"Felicidades salio la bola {bola}")
            return bola
    else:
        print(f"Salio la bola {bola}")

def completa_col(bola, carton):
    counter1=0
    counter2=0
    counter3=0
    counter4=0
    counter5=0
    for i in range(len(carton)):
       if(bola in carton[i]):
            print("hola")
            indice=j
            if indice==0:
                counter1+=1
            elif indice==1:
                counter2+=1
            elif indice==2:
                counter3+=1
            elif indice==3:
                counter4+=1
            elif indice==4:
                counter5+=1
    print(counter1, counter2, counter3, counter4, counter5)

      