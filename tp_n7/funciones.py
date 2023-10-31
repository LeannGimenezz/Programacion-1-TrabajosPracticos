def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[min_idx] > lista[j]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i
        while j > 0 and len(lista[j - 1]) > len(actual):
            lista[j] = lista[j - 1]
            j -= 1
        lista[j] = actual
    return lista