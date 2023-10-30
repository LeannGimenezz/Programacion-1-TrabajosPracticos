ocurrencias = {}

for i in range(50):

    string = input(f"Ingrese el string {i+1}: ")
    for char in string:
        if char in ocurrencias:
            ocurrencias[char] += 1
        else:
            ocurrencias[char] = 1

for char, count in ocurrencias.items():
    print(f"'{char}':{count}")