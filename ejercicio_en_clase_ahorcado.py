import random


word_list = ["hola","como","andas"]

word_select = random.choice(word_list)

word_list_selected = list(word_select)



ahorcado_word = ""
for i in range(len(word_select)):
    ahorcado_word += "_"
    
ahorcado_word = list(ahorcado_word)
size_word = len(word_select)
    
def game_ahorcado(ahorcado_word,word_list_selected,size_word):
       
    count = 0
    lives_left = 6
    while(lives_left>0 and count < len(word_select)):
        user_letter = input("ingrese un letra para buscar: ")
        if(len(user_letter)==1):
        #La letra tiene que estar en la palabra
            if(user_letter in word_list_selected):
            #Si la letra ingresada no se repite con una ya ingresada anteriormente entra
                if(user_letter not in ahorcado_word):
                    print(f"Correcto le quedan {lives_left} vidas")
                    for i in range (size_word):
                        if (user_letter == word_list_selected[i]):
                            ahorcado_word[i] = user_letter
                            print(ahorcado_word)
                            count+=1
                            continue
                else:
                    print("La letra ya fue ingresada")
                    lives_left = lives_left - 1
                    print(lives_left)
            
            else:
                print("Letra incorrecta")
                lives_left=lives_left-1
                print(f"Vidas restantes {lives_left}")
        else:
            print("Error al ingresar la letra")
            continue
    if(lives_left>0):
        return ahorcado_word
    else:
        return ahorcado_word
    
aux_word = game_ahorcado(ahorcado_word,word_list_selected,size_word)
if ("_" in aux_word):
    print("HA PERDIDO, INTENTE LA PROXIMA VEZ!")
else:
    print("HA GANADO,FELICITACIONES ")