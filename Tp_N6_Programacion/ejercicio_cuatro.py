
num_user = int(input("Ingrese un numero: "))

num_list = [1,7,23,11,45,20,14,17,12]
nueva_list = []
for num in num_list:
    if(num < num_user):
        nueva_list.append(num)
        
print("Nueva Lista")      
for num in nueva_list:
    print(num)