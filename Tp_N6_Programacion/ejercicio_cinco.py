
num = 1
nums_list = []
while(num != 0):
    num = int(input("Ingrese un numero: "))
    if(num != 0):
        nums_list.append(num)
    else:
        break
    
lista_tuplas = []
count = 0

for num in nums_list:
    count = nums_list.count(num)
    tupla = (num,count)
    lista_tuplas.append(tupla)
    
print(lista_tuplas)
