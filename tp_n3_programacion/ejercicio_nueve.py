real_password = "contra"
user_password = ""

while(real_password != user_password):
    user_password= input("Ingrese la contraseña: ")
    if(real_password != user_password):
        print("CONTRASEÑA INCORRECTA")
    else:
        print("CORRECTO")
