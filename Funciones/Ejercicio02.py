def calcular_par_impar(numero):
    lista_de_pares = []
    lista_de_impares = []
    for i in range(0, len(numero)):
        if numero[i] % 2 == 0:
            lista_de_pares.append(numero[i])
        else:
            lista_de_impares.append(numero[i])
    return lista_de_pares, lista_de_impares



lista_de_numeros = [23, 56, 45, 33, 78, 90, 100]
lista_1, lista_2 = calcular_par_impar(lista_de_numeros)
print(lista_1, lista_2)

