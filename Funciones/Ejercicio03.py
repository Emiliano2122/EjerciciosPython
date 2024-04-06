def mas_repetido(lista):
    conteo = {}
    for num in lista:
        if num in conteo:
            conteo[num] += 1
        else:
            conteo[num] = 1
    
    mas_comun = None
    repeticiones = 0
    for num, freq in conteo.items():
        if freq > repeticiones:
            mas_comun = num
            repeticiones = freq
    return mas_comun, repeticiones

numeros = [1, 2, 3, 4, 5, 1, 2, 2, 3, 4, 4, 4, 5, 5, 4, 5]
numero_mas_repetido, repeticiones = mas_repetido(numeros)
print(f"El numero que mas se repite es {numero_mas_repetido}, que aparece {repeticiones} veces.")